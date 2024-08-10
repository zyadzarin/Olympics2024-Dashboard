from django.urls import path, include
from . import views
from .views import MedallistsStatsView, CountryMedalsView, CountryMedalsHistoryView

urlpatterns = [
  path('general_stats/', MedallistsStatsView.as_view(), name='medallists-stats'),
  path('country_medals/', CountryMedalsView.as_view(), name='country-medals'),
  path('events', views.sport_list, name='events'),
  
  path('country_medals_history/', CountryMedalsHistoryView.as_view(), name='country-medals-history'),
]


