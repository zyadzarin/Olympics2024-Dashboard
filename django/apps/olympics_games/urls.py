from django.urls import path, include
from . import views
from .views import MedallistsStatsView, CountryMedalsView, CountryMedalsHistoryView, TopMedallistListView, SportListView

urlpatterns = [
  path('general_stats/', MedallistsStatsView.as_view(), name='medallists-stats'),
  path('country_medals/', CountryMedalsView.as_view(), name='country-medals'),
  path('sports/', SportListView.as_view(), name='sports'),
  path('top_medallists/', TopMedallistListView.as_view(), name='top-medallists'),
  path('country_medals_history/', CountryMedalsHistoryView.as_view(), name='country-medals-history'),
  
]


