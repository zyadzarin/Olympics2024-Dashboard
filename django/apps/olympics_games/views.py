from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from .models import Events, Athletes, Medals, MedalsTotal
from django.db.models import Q

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