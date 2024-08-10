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
  
class MedallistSerializer(serializers.ModelSerializer):
  age = serializers.SerializerMethodField()
  gold = serializers.SerializerMethodField()
  silver = serializers.SerializerMethodField()
  bronze = serializers.SerializerMethodField()

  class Meta:
    model = Medallists
    fields = ['name', 'gender', 'nationality', 'country_code', 'event', 'age', 'gold', 'silver', 'bronze']

  def get_age(self, obj):
    if obj.birth_date:
      today = date.today()
      return today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))
    return None

  def get_gold(self, obj):
    return Medallists.objects.filter(name=obj.name, medal_type='Gold').count()

  def get_silver(self, obj):
    return Medallists.objects.filter(name=obj.name, medal_type='Silver').count()

  def get_bronze(self, obj):
    return Medallists.objects.filter(name=obj.name, medal_type='Bronze').count()