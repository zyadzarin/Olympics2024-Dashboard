from django.db import models

# Create your models here.
class Results3X3Basketball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_3x3basketball'


class ResultsArchery(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_archery'


class ResultsArtisticGymnastics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_artistic_gymnastics'


class ResultsArtisticSwimming(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=4, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=4, blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_artistic_swimming'


class ResultsAthletics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  bib = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_athletics'


class ResultsBadminton(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_badminton'


class ResultsBasketball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_basketball'


class ResultsBeachVolleyball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_beach_volleyball'


class ResultsBoxing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_boxing'


class ResultsCanoeSlalom(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_canoe_slalom'


class ResultsCanoeSprint(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_canoe_sprint'


class ResultsCyclingBmxFreestyle(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_bmx_freestyle'


class ResultsCyclingBmxRacing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_bmx_racing'


class ResultsCyclingMountainBike(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TimeField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_mountain_bike'


class ResultsCyclingRoad(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_road'


class ResultsCyclingTrack(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_cycling_track'


class ResultsDiving(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_diving'


class ResultsEquestrian(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_equestrian'


class ResultsFencing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_fencing'


class ResultsFootball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_football'


class ResultsGolf(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_golf'


class ResultsHandball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_handball'


class ResultsHockey(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_hockey'


class ResultsJudo(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_judo'


class ResultsMarathonSwimming(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TimeField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_marathon_swimming'


class ResultsModernPentathlon(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_modern_pentathlon'


class ResultsRhythmicGymnastics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_rhythmic_gymnastics'


class ResultsRowing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_rowing'


class ResultsRugbySevens(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_rugby_sevens'


class ResultsSailing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_sailing'


class ResultsShooting(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_shooting'


class ResultsSkateboarding(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_skateboarding'


class ResultsSportClimbing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_sport_climbing'


class ResultsSurfing(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_surfing'


class ResultsSwimming(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TextField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_swimming'


class ResultsTableTennins(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_table_tennins'


class ResultsTaekwondo(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_taekwondo'


class ResultsTennis(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_tennis'


class ResultsTrampolineGymnastics(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_diff = models.DecimalField(max_digits=38, decimal_places=3, blank=True, null=True)
  qualification_mark = models.TextField(blank=True, null=True)
  start_order = models.TextField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_trampoline_gymnastics'


class ResultsTriathlon(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.TimeField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  result_diff = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_triathlon'


class ResultsVolleyball(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_volleyball'


class ResultsWaterPolo(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.TextField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_water_polo'


class ResultsWeightlifting(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  rank = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_type = models.TextField(blank=True, null=True)
  result_irm = models.TextField(blank=True, null=True)
  start_order = models.BigIntegerField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_weightlifting'


class ResultsWrestling(models.Model):
  date = models.TextField(blank=True, null=True)  # This field type is a guess.
  stage_code = models.TextField(blank=True, null=True)
  event_code = models.TextField(blank=True, null=True)
  event_name = models.TextField(blank=True, null=True)
  event_stage = models.TextField(blank=True, null=True)
  stage = models.TextField(blank=True, null=True)
  stage_status = models.TextField(blank=True, null=True)
  gender = models.TextField(blank=True, null=True)
  discipline_name = models.TextField(blank=True, null=True)
  discipline_code = models.TextField(blank=True, null=True)
  venue = models.TextField(blank=True, null=True)
  participant_code = models.BigIntegerField(blank=True, null=True)
  participant_name = models.TextField(blank=True, null=True)
  participant_type = models.TextField(blank=True, null=True)
  participant_country_code = models.TextField(blank=True, null=True)
  participant_country = models.TextField(blank=True, null=True)
  result = models.BigIntegerField(blank=True, null=True)
  result_wlt = models.TextField(blank=True, null=True)
  bib = models.BigIntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'results_wrestling'