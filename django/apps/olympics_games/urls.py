from django.urls import path, include
from . import views

urlpatterns = [
  path('rank_country_by_medals', views.rank_country_by_medals, name='rank_country_by_medals'),
]
