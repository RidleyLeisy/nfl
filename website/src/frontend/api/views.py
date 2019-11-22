from rest_framework import viewsets, filters
from frontend.models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from rest_framework.response import Response


class GamesReadView(viewsets.ViewSet):
	
	permission_classes = [IsAdminUser]

	def list(self, request):
		team_name = self.request.query_params.get('team_name')
		query_set = Games.objects.filter(Q(h=team_name) | Q(v=team_name))
		serializer = GamesSerializer(query_set, many=True)
		return Response(serializer.data)


class PlaysFlatReadView(viewsets.ViewSet):
	
	permission_classes = [IsAdminUser]
	
	def list(self, request):
		game_id = self.request.query_params.get('game_id')
		query_set = PlaysFlat.objects.filter(gid=game_id)
		serializer = PlaysFlatSerializer(query_set, many=True)
		return Response(serializer.data)


class TeamStatsReadView(viewsets.ViewSet):
	permissions_class = [IsAdminUser]

	def list(self, request):
		team_name = self.request.query_params.get('team_name')
		query_set = Teams.objects.filter(tname=team_name)
		serializer = TeamStatsSerializer(query_set, many=True)
		return Response(serializer.data)


class PlayerPositionReadView(viewsets.ViewSet):
	serializer_class = PlayerPositionSerializer
	permission_classes = [IsAdminUser]

	def list(self, request):
		player_name = self.request.query_params.get('player_name')
		query_set = Player.objects.filter(Q(fname=player_name))
		serializer = PlayerPositionSerializer(query_set, many=True)
		return Response(serializer.data)