from rest_framework import serializers
from .models import Medallists, MedalsTotal
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

# {
#   {
#  “country”:”United States of America”,
#  “country_code”:”USA”,
#  "medals_history":{
#   {
#   “Year”:”1896”,
#   “Bronze”:30,
#   “Silver”:34,
#   “Gold”:23,
#   "Total":87
#   },
#     {
#   “Year”:”2024”,
#   “Bronze”:30,
#   “Silver”:34,
#   “Gold”:27,
#   "Total":91
#   },
#   }
#   },
#   {
#   “country”:”United Kingdom”,
#   “country_code”:”GBR”,
#   "medals_history":{
#   {
#   “Year”:”1896”,
#   “Bronze”:30,
#   “Silver”:34,
#   “Gold”:23,
#   "Total":87
#   },
#     {
#   “Year”:”2024”,
#   “Bronze”:30,
#   “Silver”:34,
#   “Gold”:27,
#   "Total":91
#   },
# }}}

class SportSerializer(serializers.Serializer):
    sport = serializers.CharField()
    sport_code = serializers.CharField()
    total_participants = serializers.IntegerField()
    total_medals = serializers.IntegerField()
    total_gold = serializers.IntegerField()
    total_silver = serializers.IntegerField()
    total_bronze = serializers.IntegerField()
  
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



class MedalSerializer(serializers.Serializer):
    medal_type = serializers.CharField()
    discipline = serializers.CharField()
    event = serializers.CharField()

class AthleteSerializer(serializers.Serializer):
    name = serializers.CharField()
    medals = MedalSerializer(many=True)

class CountrySerializer(serializers.Serializer):
    country_code = serializers.CharField()
    total = serializers.IntegerField()
    gold_medal = serializers.IntegerField()
    silver_medal = serializers.IntegerField()
    bronze_medal = serializers.IntegerField()
    athletes = AthleteSerializer(many=True)

class TopCountriesAthletesSerializer(serializers.Serializer):
    top_countries = CountrySerializer(many=True)