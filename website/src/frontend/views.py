from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from frontend.models import Conversions, Blocks

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def teams_view(request, *args, **kwargs):
    return render(request, "teams.html", {})


def players_view(request, *args, **kwargs):
    return render(request, "players.html", {})


def twitter_view(request, *args, **kwargs):
    return render(request, "twitter.html", {})


def blocks_api(request, *args, **kwargs):
    blocks = Blocks.objects.all()
    data = serializers.serialize('json',blocks)

    return HttpResponse(data, content_type="application/json")