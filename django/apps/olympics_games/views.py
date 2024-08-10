from django.db.models import Count, Q
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events, Medals, Athletes, Medallists, MedalsTotal, MedalsTally
from .serializers import MedallitstsStatsSerializer, CountryMedalsSerializer, CountryMedalsHistorySerializer

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
  
# class CountryMedalsView(APIView):
#   def get(self, request):
#     # Get top 5 countries by total medals
#     top_5_medals = MedalsTotal.objects.order_by('-total')[:5]

#     # Get athlete counts for these top 5 countries
#     country_codes = [medal.country_code for medal in top_5_medals]
#     athlete_counts = Athletes.objects.filter(country_code__in=country_codes)\
#                       .values('country_code')\
#                       .annotate(athletes_num=Count('code'))

#     # Combine the data
#     combined_data = []
#     for medal in top_5_medals:
#       athlete_count = next((item for item in athlete_counts if item['country_code'] == medal.country_code), None)
#       country = Athletes.objects.filter(country_code=medal.country_code).values_list('country', flat=True).first() or ''
#       country_data = {
#         'country_code': medal.country_code,
#         'country': country,
#         'gold': medal.gold_medal or 0,
#         'silver': medal.silver_medal or 0,
#         'bronze': medal.bronze_medal or 0,
#         'total': medal.total or 0,
#         'athletes_num': athlete_count['athletes_num'] if athlete_count else 0
#       }
#       combined_data.append(country_data)

#     serializer = CountryMedalsSerializer(combined_data, many=True)
#     return Response(serializer.data)

class CountryMedalsView(APIView):
  def get(self, request):
    # Get medal counts from MedalsTotal
    medals_data = MedalsTotal.objects.all()

    # Get athlete counts from Athletes
    athlete_counts = Athletes.objects.values('country_code').annotate(athletes_num=Count('code'))

    # Combine the data
    combined_data = []
    for medal in medals_data:
      athlete_count = next((item for item in athlete_counts if item['country_code'] == medal.country_code), None)
      country_data = {
        'country_code': medal.country_code,
        'country': Athletes.objects.filter(country_code=medal.country_code).values_list('country', flat=True).first() or '',
        'gold': medal.gold_medal or 0,
        'silver': medal.silver_medal or 0,
        'bronze': medal.bronze_medal or 0,
        'total': medal.total or 0,
        'athletes_num': athlete_count['athletes_num'] if athlete_count else 0
      }
      combined_data.append(country_data)

    # Sort the data by total medals (descending)
    combined_data.sort(key=lambda x: x['total'], reverse=True)

    serializer = CountryMedalsSerializer(combined_data, many=True)
    return Response(serializer.data)


@cache_page(60 * 5)    # Cache the response for 5 minutes
def sport_list(request):
  # Get all sports with their codes
  sports = list(Events.objects.values('sport', 'sport_code').distinct())

  # Create a dictionary to store sport data
  sport_data = {sport['sport']: {
    'sport': sport['sport'],
    'sport_code': sport['sport_code'],
    'total_participants': 0,
    'total_medals': 0,
    'total_gold': 0,
    'total_silver': 0,
    'total_bronze': 0
  } for sport in sports}

  # Count participants
  for sport in sports:
    sport_name = sport['sport']
    events = Events.objects.filter(sport=sport_name).values_list('event', flat=True)
    participants = Athletes.objects.filter(
      Q(disciplines__icontains=sport_name) | 
      Q(events__icontains=sport_name) |
      Q(disciplines__in=events) | 
      Q(events__in=events)
    ).distinct().count()
    sport_data[sport_name]['total_participants'] = participants

  # Count medals
  for sport in sports:
    sport_name = sport['sport']
    events = Events.objects.filter(sport=sport_name).values_list('event', flat=True)
    
    medal_counts = Medals.objects.filter(
      Q(discipline__icontains=sport_name) |
      Q(event__icontains=sport_name) |
      Q(discipline__in=events) |
      Q(event__in=events)
    ).values('medal_type').annotate(count=Count('code'))

    for item in medal_counts:
      sport_data[sport_name]['total_medals'] += item['count']
      if item['medal_type'] == 'Gold Medal':
        sport_data[sport_name]['total_gold'] += item['count']
      elif item['medal_type'] == 'Silver Medal':
        sport_data[sport_name]['total_silver'] += item['count']
      elif item['medal_type'] == 'Bronze Medal':
        sport_data[sport_name]['total_bronze'] += item['count']

  # Convert the dictionary to a list of values
  sport_list = list(sport_data.values())

  # Return the data as JSON response
  return JsonResponse({'sports': sport_list}, encoder=DjangoJSONEncoder)

class CountryMedalsHistoryView(APIView):
  def get(self, request):
    # Get all countries from MedalsTotal
    countries = MedalsTotal.objects.all()

    combined_data = []
    for country in countries:
      # Get past years' data
      past_medals = MedalsTally.objects.filter(country_noc=country.country_code)\
        .values('year', 'gold', 'silver', 'bronze', 'total')\
        .order_by('year')

      # Add 2024 data
      medals_history = list(past_medals) + [{
        'year': 2024,
        'gold': country.gold_medal or 0,
        'silver': country.silver_medal or 0,
        'bronze': country.bronze_medal or 0,
        'total': country.total or 0
      }]

      country_data = {
        'country_code': country.country_code,
        'country': MedalsTally.objects.filter(country_noc=country.country_code).values_list('country', flat=True).first() or '',
        'medals_history': medals_history
      }
      combined_data.append(country_data)

    serializer = CountryMedalsHistorySerializer(combined_data, many=True)
    return Response(serializer.data)