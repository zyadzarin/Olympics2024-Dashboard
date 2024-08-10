from rest_framework import serializers
from .models import Medallists

class MedallitstsStatsSerializer(serializers.Serializer):
  participants_count = serializers.IntegerField()
  countries_count = serializers.IntegerField()
  medals_count = serializers.IntegerField()
  events_count = serializers.IntegerField()
  
class CountryMedalsSerializer(serializers.Serializer):
  country_code = serializers.CharField()
  country = serializers.CharField()
  country_full = serializers.CharField()
  gold = serializers.IntegerField()
  silver = serializers.IntegerField()
  bronze = serializers.IntegerField()
  total = serializers.IntegerField()
  athletes_num = serializers.IntegerField()
  
class YearlyMedalsSerializer(serializers.Serializer):
  year = serializers.IntegerField()
  gold = serializers.IntegerField()
  silver = serializers.IntegerField()
  bronze = serializers.IntegerField()
  total = serializers.IntegerField()

class CountryMedalsHistorySerializer(serializers.Serializer):
  country_code = serializers.CharField()
  country = serializers.CharField()
  medals_history = YearlyMedalsSerializer(many=True)