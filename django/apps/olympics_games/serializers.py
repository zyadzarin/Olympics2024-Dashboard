from rest_framework import serializers
from .models import Medallists
from datetime import date

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
  
class TopMedallistSerializer(serializers.Serializer):
  name = serializers.CharField()
  gender = serializers.CharField()
  nationality = serializers.CharField()
  country_code = serializers.CharField()
  event = serializers.CharField()
  birth_date = serializers.DateField()
  age = serializers.SerializerMethodField()
  gold = serializers.IntegerField()
  silver = serializers.IntegerField()
  bronze = serializers.IntegerField()
  total_medals = serializers.IntegerField()

  def get_age(self, obj):
    if obj['birth_date']:
      today = date.today()
      return today.year - obj['birth_date'].year - ((today.month, today.day) < (obj['birth_date'].month, obj['birth_date'].day))
    return None