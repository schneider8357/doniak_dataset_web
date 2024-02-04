"""
URL configuration for doniak_dataset_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dataset_editor.views import editor, list_oeuvres, edit_one, index, export_json

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
    # path("editor/", editor, name='editor'),
    path("oeuvres/", list_oeuvres, name='list_oeuvres'),
    path("edit_one/", edit_one, name='edit_one'),
    path("export/", export_json, name='export_json'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
