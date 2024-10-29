from django.db import models # type: ignore

class Sponsor(models.Model):
    name = models.CharField(max_length=255)


class Study(models.Model):
    study_id = models.AutoField(primary_key=True)
    study_name = models.CharField(max_length=100)
    study_description = models.TextField()
    study_phase = models.CharField(max_length=10, choices=[
        ('Phase I', 'Phase one'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ])
    sponsor_name_id = models.CharField(max_length=255)

