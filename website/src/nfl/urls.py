"""nfl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from frontend.views import *
from frontend.api.views import *
from .router import router

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    path('teams', team_view, name='teams'),
    path('teams/offense', offense_team_view, name='offense'),
    path('teams/defense', defense_team_view, name='defense'),
    path('players', player_view, name='players'),
    path('players/db', db_view, name='db'),
    path('players/dl', dl_view, name='dl'),
    path('players/kicker', kicker_view, name='kicker'),
    path('players/ol', ol_view, name='ol'),
    path('players/qb', qb_view, name='qb'),
    path('players/rb', rb_view, name='rb'),
    path('players/te', te_view, name='te'),
    path('players/wr', wr_view, name='wr'),
    path('players/lb', lb_view, name='lb'),
    path('matchups', matchup_view, name='matchups'),
    path('admin/', admin.site.urls),
    # api views
    path('api/',include(router.urls)),
    ]
