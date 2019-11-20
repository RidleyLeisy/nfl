from rest_framework import generics
from frontend.models import Games, PlaysFlat
from .serializers import GamesSerializer, PlaysFlatSerializer, TouchdownsFlatSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import filters  
from django.db.models import Q


class GamesReadView(generics.ListAPIView):
	serializer_class = GamesSerializer
	permission_classes = [IsAdminUser]

	def get_queryset(self):
		team_name = self.kwargs['team_name']
		return Games.objects.filter(Q(h=team_name) | Q(v=team_name))


class PlaysFlatReadView(generics.ListAPIView):
	serializer_class = PlaysFlatSerializer
	permission_classes = [IsAdminUser]
	
	def get_queryset(self):
		game_id = self.kwargs['game_id']
		return PlaysFlat.objects.filter(gid=game_id)


class TouchdownsReadView(generics.ListAPIView):
	serializer_class = TouchdownsFlatSerializer
	permissions_class = [IsAdminUser]

	def get_queryset(self):
		team_name = self.kwargs['team_name']
		Games.objects.filter(Q(h=team_name) | Q(v=team_name))
		return
		
class PlayerPositionReadView(generics.ListAPIView):
	serializer_class = PlayerPositionSerializer
	permission_classes = [IsAdminUser]