from django.db import models

# # Create your models here.
class Athletes(models.Model):
  code = models.BigIntegerField(blank=True, primary_key=True)
  name = models.TextField(blank=True, null=True)
  name_short = models.TextField(blank=True, null=True)
  name_tv = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  function = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  country = models.TextField(blank=True, null=True)
  country_full = models.TextField(blank=True, null=True)
  nationality = models.TextField(blank=True, null=True)
  nationality_full = models.TextField(blank=True, null=True)
  nationality_code = models.TextField(blank=True, null=True)
  height = models.BigIntegerField(blank=True, null=True)
  weight = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  disciplines = models.TextField(blank=True, null=True)
  events = models.TextField(blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)
  birth_place = models.TextField(blank=True, null=True)
  birth_country = models.TextField(blank=True, null=True)
  residence_place = models.TextField(blank=True, null=True)
  residence_country = models.TextField(blank=True, null=True)
  nickname = models.TextField(blank=True, null=True)
  hobbies = models.TextField(blank=True, null=True)
  occupation = models.TextField(blank=True, null=True)
  education = models.TextField(blank=True, null=True)
  family = models.TextField(blank=True, null=True)
  lang = models.TextField(blank=True, null=True)
  coach = models.TextField(blank=True, null=True)
  reason = models.TextField(blank=True, null=True)
  hero = models.TextField(blank=True, null=True)
  influence = models.TextField(blank=True, null=True)
  philosophy = models.TextField(blank=True, null=True)
  sporting_relatives = models.TextField(blank=True, null=True)
  ritual = models.TextField(blank=True, null=True)
  other_sports = models.TextField(blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'athletes'
    
class Events(models.Model):
  event = models.TextField(blank=True, primary_key=True)
  tag = models.TextField(blank=True, null=True)
  sport = models.TextField(blank=True, null=True)
  sport_code = models.TextField(blank=True, null=True)
  sport_url = models.TextField(blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'events'


class Medallists(models.Model):
  code = models.TextField(blank=True, primary_key=True)
  medal_date = models.DateField(blank=True, null=True)
  medal_type = models.TextField(blank=True, null=True)
  medal_code = models.BigIntegerField(blank=True, null=True)
  name = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  country = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  nationality = models.TextField(blank=True, null=True)
  team = models.TextField(blank=True, null=True)
  team_gender = models.TextField(blank=True, null=True)
  discipline = models.TextField(blank=True, null=True)
  event = models.TextField(blank=True, null=True)
  event_type = models.TextField(blank=True, null=True)
  url_event = models.TextField(blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'medallists'


class Medals(models.Model):
  code = models.TextField(blank=True, primary_key=True)
  medal_type = models.TextField(blank=True, null=True)
  medal_code = models.BigIntegerField(blank=True, null=True)
  medal_date = models.DateField(blank=True, null=True)
  name = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline = models.TextField(blank=True, null=True)
  event = models.TextField(blank=True, null=True)
  event_type = models.TextField(blank=True, null=True)
  url_event = models.TextField(blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'medals'


class MedalsTotal(models.Model):
  country_code = models.TextField(blank=True, primary_key=True)
  gold_medal = models.BigIntegerField(blank=True, null=True)
  silver_medal = models.BigIntegerField(blank=True, null=True)
  bronze_medal = models.BigIntegerField(blank=True, null=True)
  total = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'medals_total'


# class Schedules(models.Model):
#   start_date = models.DateTimeField(blank=True, null=True)
#   end_date = models.DateTimeField(blank=True, null=True)
#   day = models.DateField(blank=True, null=True)
#   status = models.TextField(blank=True, null=True)
#   discipline = models.TextField(blank=True, null=True)
#   discipline_code = models.TextField(blank=True, null=True)
#   event = models.TextField(blank=True, null=True)
#   event_medal = models.BigIntegerField(blank=True, null=True)
#   phase = models.TextField(blank=True, null=True)
#   gender = models.TextField(blank=True, null=True)
#   event_type = models.TextField(blank=True, null=True)
#   venue = models.TextField(blank=True, null=True)
#   venue_code = models.TextField(blank=True, null=True)
#   location_description = models.TextField(blank=True, null=True)
#   location_code = models.TextField(blank=True, null=True)
#   url = models.TextField(blank=True, null=True)

#   class Meta:
#     managed = True
#     db_table = 'schedules'


# class SchedulesPreliminary(models.Model):
#   id = models.BigAutoField(primary_key=True)
#   date_start_utc = models.DateTimeField(blank=True, null=True)
#   date_end_utc = models.DateTimeField(blank=True, null=True)
#   estimated = models.BooleanField(blank=True, null=True)
#   estimated_start = models.BooleanField(blank=True, null=True)
#   start_text = models.TimeField(blank=True, null=True)
#   medal = models.BigIntegerField(blank=True, null=True)
#   venue_code = models.TextField(blank=True, null=True)
#   description = models.TextField(blank=True, null=True)
#   venue_code_other = models.TextField(blank=True, null=True)
#   discription_other = models.TextField(blank=True, null=True)
#   team_1_code = models.TextField(blank=True, null=True)
#   team_1 = models.TextField(blank=True, null=True)
#   team_2_code = models.TextField(blank=True, null=True)
#   team_2 = models.TextField(blank=True, null=True)
#   tag = models.TextField(blank=True, null=True)
#   sport = models.TextField(blank=True, null=True)
#   sport_code = models.TextField(blank=True, null=True)
#   sport_url = models.TextField(blank=True, null=True)

#   class Meta:
#     managed = True
#     db_table = 'schedules_preliminary'


class Teams(models.Model):
  code = models.TextField(blank=True, primary_key=True)
  team = models.TextField(blank=True, null=True)
  team_gender = models.TextField(blank=True, null=True)
  country = models.TextField(blank=True, null=True)
  country_full = models.TextField(blank=True, null=True)
  country_code = models.TextField(blank=True, null=True)
  discipline = models.TextField(blank=True, null=True)
  disciplines_code = models.TextField(blank=True, null=True)
  events = models.TextField(blank=True, null=True)
  athletes = models.TextField(blank=True, null=True)
  coaches = models.TextField(blank=True, null=True)
  athletes_codes = models.TextField(blank=True, null=True)
  num_athletes = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  coaches_codes = models.TextField(blank=True, null=True)
  num_coaches = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'teams'


class TorchRoute(models.Model):
  title = models.TextField(blank=True, primary_key=True)
  city = models.TextField(blank=True, null=True)
  date_start = models.DateTimeField(blank=True, null=True)
  date_end = models.DateTimeField(blank=True, null=True)
  tag = models.TextField(blank=True, null=True)
  url = models.TextField(blank=True, null=True)
  stage_number = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'torch_route'


class Venues(models.Model):
  venue = models.TextField(blank=True, primary_key=True)
  sports = models.TextField(blank=True, null=True)
  date_start = models.DateTimeField(blank=True, null=True)
  date_end = models.DateTimeField(blank=True, null=True)
  tag = models.TextField(blank=True, null=True)
  url = models.TextField(blank=True, null=True)

  class Meta:
    managed = True
    db_table = 'venues'