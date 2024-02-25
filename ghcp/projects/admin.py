import json
from typing import Any
from django import forms
from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponseNotAllowed
from django.http.response import HttpResponse

from .utils import get_projects

from .models import Project
from django.shortcuts import render


class ProForm(forms.ModelForm):
    project = forms.ChoiceField(choices=[(json.dumps(r), r["name"]) for r in get_projects()])
    created_at = forms.DateTimeField()

    class Meta:
        model = Project
        fields = ["pet", "project", "image", "name", "link", "demo", "tools", "description", "created_at"]



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProForm
    
