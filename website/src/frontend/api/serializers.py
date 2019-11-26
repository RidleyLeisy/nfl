from rest_framework import serializers
from frontend.models import *

# Convert Querysets to Json and Validate 

class GamesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Games
		fields = '__all__'
		

class PlayerPositionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = '__all__'


class TeamStatsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teams
		fields = '__all__'
	

class OffenseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offense
		fields = '__all__'


class PassingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Passing
		fields = '__all__'


class TouchdownSerializer(serializers.ModelSerializer):
	class Meta:
		model = Touchdowns
		fields = '__all__'