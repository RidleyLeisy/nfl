from rest_framework import viewsets, filters
from frontend.models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from rest_framework.response import Response
import re


class GamesReadView(viewsets.ViewSet):
	
	permission_classes = [IsAdminUser]

	def list(self, request):
		team_name = self.request.query_params.get('team_name')
		query_set = Games.objects.filter(Q(h=team_name) | Q(v=team_name))
		serializer = GamesSerializer(query_set, many=True)
		return Response(serializer.data)


class TeamStatsReadView(viewsets.ViewSet):
	permissions_class = [IsAdminUser]

	def list(self, request):
		team_name = self.request.query_params.get('team_name')
		query_set = Teams.objects.filter(tname=team_name)
		serializer = TeamStatsSerializer(query_set, many=True)
		return Response(serializer.data)


class PlayerPositionReadView(viewsets.ViewSet):
	permission_classes = [IsAdminUser]

	def list(self, request):
		player_name = self.request.query_params.get('player_name')
		player_name = re.findall('[A-Z][^A-Z]*', player_name) # Split name based on capital letters
		query_set = Player.objects.filter(Q(fname=player_name[0]) & Q(lname=player_name[1]))
		serializer = PlayerPositionSerializer(query_set, many=True)
		return Response(serializer.data)


class OffenseReadView(viewsets.ViewSet):
	permission_classes = [IsAdminUser]

	def list(self, request):
		# Option to filter by player or team/seas
		filter_by = self.request.query_params.get('filter') # Player or Team/Season
		if filter_by == 'player':
			player_name = self.request.query_params.get('player_name')
			player_name = re.findall('[A-Z][^A-Z]*', player_name) # Split name based on capital letters
			player_id = Player.objects.filter(Q(fname=player_name[0]) & Q(lname=player_name[1])).first().player
			query_set = Offense.objects.filter(Q(player=player_id))
		if filter_by == 'team':
			team_name = self.request.query_params.get('team_name')
			season = self.request.query_params.get('season')
			query_set = Offense.objects.filter(team=team_name).filter(year=season)
		serializer = OffenseSerializer(query_set, many=True)
		return Response(serializer.data)
	

class PassingReadView(viewsets.ViewSet):
	permission_classes = [IsAdminUser]

	def list(self, request):
		filter_by = self.request.query_params.get('filter')
		if filter_by == 'qb':
			game_ids = []
			team_name = self.request.query_params.get('team_name')
			year = self.request.query_params.get('season')
			qb_id = Player.objects.filter(Q(cteam=team_name) & Q(pos1='QB') & Q(dcp=1)).first().player
			game_ids_query_set = Games.objects.filter(Q(seas=year) & (Q(v=team_name) | Q(h=team_name)))
			for game in game_ids_query_set:
				game_ids.append(game.gid)
			query_set = PlaysFlat.objects.filter(Q(psr=qb_id) & Q(gid__in=game_ids))
			play_ids = []
			for play in query_set:
				play_ids.append(play.pid)
			query_set = Passing.objects.filter(pid__in=play_ids)
			serializer = PassingSerializer(query_set, many=True)
		if filter_by == 'wr':
			player_name = self.request.query_params.get('player_name')
			player_name = re.findall('[A-Z][^A-Z]*', player_name) # Split name based on capital letters
			player_id = Player.objects.filter(Q(fname=player_name[0]) & Q(lname=player_name[1])).first().player
			query_set = Passing.objects.filter(trg__contains=player_id)
			serializer = PassingSerializer(query_set, many=True)
		return Response(serializer.data)
		
class TouchdownReadView(viewsets.ViewSet):
	permission_classes = [IsAdminUser]

	def list(self, request):
		game_ids = []
		team_name = self.request.query_params.get('team_name')
		year = self.request.query_params.get('season')
		game_ids_query_set = Games.objects.filter(Q(seas=year) & (Q(v=team_name) | Q(h=team_name)))
		for game in game_ids_query_set:
				game_ids.append(game.gid)
		plays_query_set = PlaysFlat.objects.filter(Q(gid__in=game_ids))
		play_ids = []
		for play in plays_query_set:
			play_ids.append(play.pid)
		query_set = Touchdowns.objects.filter(pid__in=play_ids)
		serializer = TouchdownSerializer(query_set, many=True)
		return Response(serializer.data)


class OffenseStatsReadView(viewsets.ViewSet):
	permission_classes = [IsAdminUser]

	def list(self, request):
		self.request.query_params.get('year')
		return 