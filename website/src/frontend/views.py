from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from frontend.models import Conversions, Blocks, Games

# Views
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def offense_view(request, *args, **kwargs):
	return render(request, "offense.html", {})


def defense_view(request, *args, **kwargs):
    return render(request, "defense.html", {})


def twitter_view(request, *args, **kwargs):
    return render(request, "twitter.html", {})

