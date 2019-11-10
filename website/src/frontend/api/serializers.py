from rest_framework import serializers
from frontend.models import Games, PlaysFlat, Touchdowns

# Convert Querysets to Json and Validate 

class GamesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Games
		fields = '__all__'


class PlaysFlatSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlaysFlat
		fields = '__all__'

class TouchdownsFlatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Touchdowns
		fields = '__all__'