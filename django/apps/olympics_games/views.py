from django.db.models import Count, Q, Subquery
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events, Athletes, Medals, Athletes, Medallists, MedalsTotal
from .serializers import MedallitstsStatsSerializer, CountryMedalsSerializer
from django.utils.decorators import method_decorator
from .models import Events, Medals, Athletes, Medallists, MedalsTotal, MedalsTally
from .serializers import MedallitstsStatsSerializer, CountryMedalsSerializer, CountryMedalsHistorySerializer, TopMedallistSerializer, SportSerializer

# Create your views here.
class MedallistsStatsView(APIView):
  @method_decorator(cache_page(60 * 10))    # Cache the response for 10 minutes
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

class CountryMedalsView(APIView):
  @method_decorator(cache_page(60 * 10))    # Cache the response for 10 minutes
  def get(self, request):
    # Get all unique countries from Athletes
    all_countries = Athletes.objects.values('country_code', 'country', 'country_full').distinct()

    # Get medal counts from MedalsTotal
    medals_data = {medal.country_code: medal for medal in MedalsTotal.objects.all()}

    # Get athlete counts
    athlete_counts = Athletes.objects.values('country_code').annotate(athletes_num=Count('code'))
    athlete_counts_dict = {item['country_code']: item['athletes_num'] for item in athlete_counts}

    # Combine the data
    combined_data = []
    for country in all_countries:
      medal_info = medals_data.get(country['country_code'], None)
      country_data = {
        'country_code': country['country_code'],
        'country': country['country'] or '',
        'country_full': country['country_full'] or '',
        'gold': medal_info.gold_medal if medal_info else 0,
        'silver': medal_info.silver_medal if medal_info else 0,
        'bronze': medal_info.bronze_medal if medal_info else 0,
        'total': medal_info.total if medal_info else 0,
        'athletes_num': athlete_counts_dict.get(country['country_code'], 0)
      }
      combined_data.append(country_data)

    # Sort the data by total medals (descending)
    combined_data.sort(key=lambda x: x['total'], reverse=True)

    serializer = CountryMedalsSerializer(combined_data, many=True)
    return Response(serializer.data)


class SportListView(APIView):
    @method_decorator(cache_page(60 * 5))  # Cache the response for 5 minutes
    def get(self, request):
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

        serializer = SportSerializer(sport_list, many=True)
        return Response({'sports': serializer.data})

class TopMedallistListView(generics.ListAPIView):
  serializer_class = TopMedallistSerializer

  def get_queryset(self):
    # Subquery to get the top 100 athletes by total medal count
    top_athletes = Medallists.objects.values('name')\
      .annotate(total_medals=Count('medal_type'))\
      .order_by('-total_medals')[:100]

    # Main query to get detailed information for the top 100 athletes
    return Medallists.objects.filter(name__in=Subquery(top_athletes.values('name')))\
      .values('name', 'gender', 'nationality', 'country_code', 'event', 'birth_date')\
      .annotate(
        gold=Count('medal_type', filter=Q(medal_type='Gold Medal')),
        silver=Count('medal_type', filter=Q(medal_type='Silver Medal')),
        bronze=Count('medal_type', filter=Q(medal_type='Bronze Medal')),
        total_medals=Count('medal_type')
      )\
      .order_by('-total_medals', '-gold', '-silver', '-bronze')

class CountryMedalsHistoryView(APIView):
  @method_decorator(cache_page(60 * 5))  # Cache the response for 5 minutes
  def get(self, request):
    country_code = request.query_params.get('country_code')

    if country_code:
      # If country_code is provided, fetch data for that country only
      country = MedalsTotal.objects.filter(country_code=country_code).first()
      if not country:
        return Response({"error": "Country not found"}, status=404)
      
      combined_data = [self.get_country_data(country)]
    else:
      # If no country_code is provided, fetch data for all countries
      countries = MedalsTotal.objects.all()
      combined_data = [self.get_country_data(country) for country in countries]

    serializer = CountryMedalsHistorySerializer(combined_data, many=True)
    return Response(serializer.data)

  def get_country_data(self, country):
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

    return {
      'country_code': country.country_code,
      'country': MedalsTally.objects.filter(country_noc=country.country_code).values_list('country', flat=True).first() or '',
      'medals_history': medals_history
    }