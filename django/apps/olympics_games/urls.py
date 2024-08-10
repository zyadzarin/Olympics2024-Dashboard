from django.urls import path, include
from . import views
from .views import MedallistsStatsView

urlpatterns = [
  path('general-stats/', MedallistsStatsView.as_view(), name='medallists-stats'),
  path('rank_country_by_medals', views.rank_country_by_medals, name='rank_country_by_medals'),
  path('events', views.sport_list, name='events'),
]


