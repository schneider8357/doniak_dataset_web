import re
import json
import traceback
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponseNotAllowed, HttpResponse
from django.core.paginator import Paginator

from .models import Personne, Oeuvre, Episode
from .forms import OeuvreFilterForm


def index(request):
    return render(request, "index.html")

def list_oeuvres(request):
    if request.method != "GET":
        return HttpResponseNotAllowed()
    form = OeuvreFilterForm(request.GET)
    oeuvres = Oeuvre.objects.all()
    p = request.GET.get("p", 1)
    items_per_page = 25
    if form.is_valid():
        for field in OeuvreFilterForm.Meta.fields:
            value = form.cleaned_data.get(field)
            if value:
                oeuvres = oeuvres.filter(**{field: value})
        order_by = form.cleaned_data.get("order_by")
        if order_by:
            if form.cleaned_data.get("desc"):
                order_by = "-" + order_by
            oeuvres = oeuvres.order_by(order_by)
        if form.cleaned_data.get("items_per_page"):
            items_per_page = form.cleaned_data.get("items_per_page")
    paginator = Paginator(oeuvres, items_per_page)
    page = paginator.page(p)
    return render(
        request,
        "list_oeuvres.html",
        {"form": form, "page": page, "oeuvre_fields": Oeuvre._meta.get_fields()},
    )

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
        return render(request, "editor.html", {"json_data": get_object_or_404(Oeuvre, oeuvre_num_livres=request.GET.get("oeuvre_num_livres")).to_json()})
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
            obj_oeuvre = get_object_or_404(Oeuvre, oeuvre_num_livres=dict_oeuvre["oeuvre_num_livres"])
            for field, value in dict_regular_fields.items():
                setattr(obj_oeuvre, field, value)
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
