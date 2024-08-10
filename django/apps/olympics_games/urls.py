from django.urls import path, include
from . import views
from .views import MedallistsStatsView

urlpatterns = [
  path('general-stats/', MedallistsStatsView.as_view(), name='medallists-stats'),
]
