from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import MedalsTotal

# Create your views here.
@cache_page(60 * 5)    # Cache the response for 5 minutes
def rank_country_by_medals(request):
  medals_data = MedalsTotal.objects.all().order_by('-total', '-gold_medal', '-silver_medal', '-bronze_medal')
  
  # Add rank to each country
  ranked_data = []
  for rank, country in enumerate(medals_data, start=1):
      ranked_data.append({
          'rank': rank,
          'country_code': country.country_code,
          'gold_medal': country.gold_medal,
          'silver_medal': country.silver_medal,
          'bronze_medal': country.bronze_medal,
          'total': country.total
      })

  # Pass the data to the template
  response_data = {
      'ranked_data': ranked_data
  }
  return JsonResponse(response_data, encoder=DjangoJSONEncoder)