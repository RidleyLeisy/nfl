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

def team_view(request, *args, **kwargs):
	return render(request, "teams.html", {})

def offense_team_view(request, *args, **kwargs):
    return render(request, "teams/offense.html")

def defense_team_view(request, *args, **kwargs):
    return render(request, "teams/defense.html")

def player_view(request, *args, **kwargs):
    return render(request, "players.html", {})

def qb_view(request, *args, **kwargs):
    return render(request, "players/qb.html", {})

def wr_view(request, *args, **kwargs):
    return render(request, "players/wr.html", {})

def dl_view(request, *args, **kwargs):
    return render(request, "players/dl.html", {})

def ol_view(request, *args, **kwargs):
    return render(request, "players/ol.html", {})

def rb_view(request, *args, **kwargs):
    return render(request, "players/rb.html", {})

def db_view(request, *args, **kwargs):
    return render(request, "players/db.html", {})

def te_view(request, *args, **kwargs):
    return render(request, "players/te.html", {})

def lb_view(request, *args, **kwargs):
    return render(request, "players/lb.html", {})

def kicker_view(request, *args, **kwargs):
    return render(request, "players/kicker.html", {})


def matchup_view(request, *args, **kwargs):
    return render(request, "matchups.html", {})

