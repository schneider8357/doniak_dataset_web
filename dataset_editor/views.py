import re
import json
import traceback
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponseNotAllowed, HttpResponse, StreamingHttpResponse
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Personne, Oeuvre, Episode
from .forms import OeuvreFilterForm


def index(request):
    return render(request, "index.html")

def list_oeuvres(request):
    if request.method != "GET":
        return HttpResponseNotAllowed()
    form = OeuvreFilterForm(request.GET)
    oeuvres = Oeuvre.objects.all().order_by('oeuvre_num_livres')
    p = request.GET.get("p", 1)
    items_per_page = 25
    for field in OeuvreFilterForm.Meta.fields_equal:
        value = form.data.get(field)
        if value:
            oeuvres = oeuvres.filter(**{field: value})
    for field in OeuvreFilterForm.Meta.fields_contains:
        value = form.data.get(field)
        if value:
            oeuvres = oeuvres.filter(**{f"{field}__icontains": value})
    personne = form.data.get("personne")
    if personne:
        query = Q()
        for field in Oeuvre.many_to_many_fields:
            query.add(Q(**{f"{field}__full_name__icontains": personne}), Q.OR)
        oeuvres = oeuvres.filter(query).distinct("oeuvre_num_livres")
    order_by = form.data.get("order_by")
    if order_by:
        if form.data.get("desc"):
            order_by = "-" + order_by
        oeuvres = oeuvres.order_by(order_by)
    if form.data.get("items_per_page"):
        items_per_page = form.data.get("items_per_page")
    paginator = Paginator(oeuvres, items_per_page)
    page = paginator.page(p)
    return render(
        request,
        "list_oeuvres.html",
        {"form": form, "page": page, "oeuvre_fields": Oeuvre._meta.get_fields()},
    )

def get_json_generator():
    yield "["
    data = Oeuvre.objects.all().order_by('oeuvre_num_livres')
    last = data[len(data) - 1]
    for record in data[:len(data) - 1]:
        yield (json.dumps(record.to_json()) + ",").encode('utf-8')
    yield json.dumps(last.to_json()).encode('utf-8')
    yield "]"

def export_json(request):
    if request.method != "GET":
        return HttpResponseNotAllowed()
    response = StreamingHttpResponse(streaming_content=get_json_generator(), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="{0}_{1}.json"'.format(
        'oeuvres', datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
    return response

def editor(request):
    if request.method == "GET":
        return render(request, "editor.html", {"json_data": [oeuvre.to_json() for oeuvre in Oeuvre.objects.all()]})
    elif request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            for dict_oeuvre in json_data:
                dict_regular_fields = {}
                dict_many_to_many_fields = {}
                for key, val in dict_oeuvre.items():
                    if key in Oeuvre.regular_fields:
                        dict_regular_fields[key] = val if val is not None else ""
                    elif key in Oeuvre.many_to_many_fields:
                        dict_many_to_many_fields[key] = val if val is not None else ""
                match = re.search(r'\b(\d{2}).(\d{2}).(\d{4})\b', dict_regular_fields["date_diff"])
                result = match.groups() if match else None
                dict_regular_fields["date_diff"] = datetime(*([int(x) for x in result][::-1]))
                try:
                    obj_oeuvre = get_object_or_404(Oeuvre, oeuvre_num_livres=dict_oeuvre["oeuvre_num_livres"])
                    for field, value in dict_regular_fields.items():
                        setattr(obj_oeuvre, field, value)
                except Http404:
                    if not 0 < int(dict_oeuvre["oeuvre_num_livres"]) < 9000:
                        return JsonResponse({'status': 'error', 'message': 'Invalid oeuvre_num_livres'})
                    obj_oeuvre = Oeuvre.objects.create(**dict_regular_fields)
                for field in dict_many_to_many_fields:
                    personnes = []
                    for personne in dict_many_to_many_fields[field]:
                        obj_personne, created = Personne.objects.get_or_create(full_name=personne)
                        if not obj_personne.role:
                            obj_personne.role = []
                        obj_personne.role = set([field] + obj_personne.role)
                        obj_personne.save()
                        personnes.append(obj_personne)
                    getattr(obj_oeuvre, field).set(personnes)
                if dict_oeuvre.get("episodes"):
                    for dict_episode in dict_oeuvre["episodes"]:
                        ep_regular_fields = {}
                        ep_many_to_many_fields = {}
                        for key, val in dict_episode.items():
                            if key in Episode.regular_fields:
                                ep_regular_fields[key] = val if val is not None else ""
                            elif key in Episode.many_to_many_fields:
                                ep_many_to_many_fields[key] = val if val is not None else ""
                        try:
                            obj_episode = get_object_or_404(Episode, episode_num=dict_episode["episode_num"])
                            for field, value in ep_regular_fields.items():
                                setattr(obj_episode, field, value)
                            obj_episode.episode_num_part = int(ep_regular_fields["episode_num"].split(".")[1])
                        except Http404:
                            try:
                                ep_regular_fields["episode_num_part"] = int(ep_regular_fields["episode_num"].split(".")[1])
                            except IndexError as e:
                                return HttpResponse(f"{e} - {ep_regular_fields['episode_num']}", status=400)
                            obj_episode = Episode.objects.create(oeuvre=obj_oeuvre, **ep_regular_fields)
                        for field in dict_many_to_many_fields:
                            personnes = []
                            for personne in dict_many_to_many_fields[field]:
                                obj_personne, created = Personne.objects.get_or_create(full_name=personne)
                                if not obj_personne.role:
                                    obj_personne.role = []
                                obj_personne.role = set([field] + obj_personne.role)
                                obj_personne.save()
                                personnes.append(obj_personne)
                            getattr(obj_oeuvre, field).set(personnes)
                        obj_episode.save()
                obj_oeuvre.save()
            return JsonResponse({'status': 'ok'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'exception': f'{traceback.format_exc(limit=1)}'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def edit_one(request):
    if request.method == "GET":
        oeuvre = get_object_or_404(Oeuvre, oeuvre_num_livres=request.GET.get("oeuvre_num_livres")).to_json()
        return render(request, "editor.html", {"json_data": oeuvre})
    elif request.method == 'POST':
        try:
            dict_oeuvre = json.loads(request.body)
            dict_regular_fields = {}
            dict_many_to_many_fields = {}
            for key, val in dict_oeuvre.items():
                if key in Oeuvre.regular_fields:
                    dict_regular_fields[key] = val if val is not None else ""
                elif key in Oeuvre.many_to_many_fields:
                    dict_many_to_many_fields[key] = val if val is not None else ""
            match = re.search(r'\b(\d{2}).(\d{2}).(\d{4})\b', dict_regular_fields["date_diff"])
            result = match.groups() if match else None
            dict_regular_fields["date_diff"] = datetime(*([int(x) for x in result][::-1]))
            try:
                obj_oeuvre = get_object_or_404(Oeuvre, oeuvre_num_livres=dict_oeuvre["oeuvre_num_livres"])
                for field, value in dict_regular_fields.items():
                    setattr(obj_oeuvre, field, value)
            except Http404:
                if not 0 < int(dict_oeuvre["oeuvre_num_livres"]) < 9000:
                    return JsonResponse({'status': 'error', 'message': 'Invalid oeuvre_num_livres'})
                obj_oeuvre = Oeuvre.objects.create(**dict_regular_fields)
            for field in dict_many_to_many_fields:
                personnes = []
                for personne in dict_many_to_many_fields[field]:
                    obj_personne, created = Personne.objects.get_or_create(full_name=personne)
                    if not obj_personne.role:
                        obj_personne.role = []
                    obj_personne.role = set([field] + obj_personne.role)
                    obj_personne.save()
                    personnes.append(obj_personne)
                getattr(obj_oeuvre, field).set(personnes)
            if dict_oeuvre.get("episodes"):
                for dict_episode in dict_oeuvre["episodes"]:
                    ep_regular_fields = {}
                    ep_many_to_many_fields = {}
                    for key, val in dict_episode.items():
                        if key in Episode.regular_fields:
                            ep_regular_fields[key] = val if val is not None else ""
                        elif key in Episode.many_to_many_fields:
                            ep_many_to_many_fields[key] = val if val is not None else ""
                    try:
                        obj_episode = get_object_or_404(Episode, episode_num=dict_episode["episode_num"])
                        for field, value in ep_regular_fields.items():
                            setattr(obj_episode, field, value)
                        obj_episode.episode_num_part = int(ep_regular_fields["episode_num"].split(".")[1])
                    except Http404:
                        try:
                            ep_regular_fields["episode_num_part"] = int(ep_regular_fields["episode_num"].split(".")[1])
                        except IndexError as e:
                            return HttpResponse(f"{e} - {ep_regular_fields['episode_num']}", status=400)
                        obj_episode = Episode.objects.create(oeuvre=obj_oeuvre, **ep_regular_fields)
                    for field in ep_many_to_many_fields:
                        personnes = []
                        for personne in ep_many_to_many_fields[field]:
                            obj_personne, created = Personne.objects.get_or_create(full_name=personne)
                            if not obj_personne.role:
                                obj_personne.role = []
                            obj_personne.role = set([field] + obj_personne.role)
                            obj_personne.save()
                            personnes.append(obj_personne)
                        getattr(obj_episode, field).set(personnes)
                    obj_episode.save()
            obj_oeuvre.save()
            return JsonResponse({'status': 'ok'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'exception': f'{traceback.format_exc(limit=1)}'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
