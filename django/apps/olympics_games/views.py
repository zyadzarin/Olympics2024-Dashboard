from django.shortcuts import render
from django.db.models import Count, OuterRef
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Athletes, Medallists, MedalsTotal
from .serializers import MedallitstsStatsSerializer

# Create your views here.
class MedallistsStatsView(APIView):
  def get(self, request):
    participants_count = Medallists.objects.values('name').distinct().count()
    countries_count = Medallists.objects.values('country').distinct().count()
    medals_count = Medallists.objects.exclude(medal_type__isnull=True).count()
    events_count = Medallists.objects.values('event').distinct().count()

    data = {
      'participants_count': participants_count,
      'countries_count': countries_count,
      'medals_count': medals_count,
      'events_count': events_count,
    }

    serializer = MedallitstsStatsSerializer(data)
    return Response(serializer.data)
