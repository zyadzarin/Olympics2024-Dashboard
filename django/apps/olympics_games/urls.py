from django.urls import path, include
from . import views
from .views import (MedallistsStatsView, CountryMedalsView, CountryMedalsHistoryView, TopMedallistListView, SportListView, TopCountriesAthletesView
                    ,CountryInfoListView, MedalResultsView, RegisterView)

urlpatterns = [
  path('general_stats/', MedallistsStatsView.as_view(), name='medallists-stats'),
  path('country_medals/', CountryMedalsView.as_view(), name='country-medals'),
  path('sports/', SportListView.as_view(), name='sports'),
  path('top_medallists/', TopMedallistListView.as_view(), name='top-medallists'),
  path('country_medals_history/', CountryMedalsHistoryView.as_view(), name='country-medals-history'),
  path('top_countries_athletes/', TopCountriesAthletesView.as_view(), name='top-countries-athletes'),
  path('country_info/', CountryInfoListView.as_view(), name='country-info'),
  path('medal_results/', MedalResultsView.as_view(), name='medal-results'),
  # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('register/', RegisterView.as_view(), name='auth_register'),
]


