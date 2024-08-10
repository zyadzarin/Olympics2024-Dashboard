from rest_framework import serializers
from .models import Medallists

class MedallitstsStatsSerializer(serializers.Serializer):
  participants_count = serializers.IntegerField()
  countries_count = serializers.IntegerField()
  medals_count = serializers.IntegerField()
  events_count = serializers.IntegerField()