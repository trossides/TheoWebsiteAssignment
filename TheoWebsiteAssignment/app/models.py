"""
Definition of models.
"""

from django.db import models
from django import forms;

# Create your models here.
class Club(models.Model):
    name = models.CharField("club",max_length=50)
    year_formed = models.PositiveIntegerField()
    president_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club;
        fields = ['name', 'year_formed', 'president_name', 'email', 'phone_number'];

class Team(models.Model):
    name = models.CharField("team",max_length=50)
    about = models.CharField(max_length=500)
    training_time = models.CharField(max_length=100)
    club = models.ForeignKey(Club)