"""
Definition of models.
"""

from django.db import models
from django import forms;

# Class models.
class Club(models.Model):
    name = models.CharField("club",max_length=50, help_text='Name of the Club.')
    year_formed = models.PositiveIntegerField(help_text='The year the Club was formed.')
    president_name = models.CharField(max_length=25, help_text='The president name of the Club.')
    email = models.EmailField(help_text='The contact email address for the Club.')
    phone_number = models.CharField(max_length=12, help_text='The phone number to contact the Club.')
    club_nickname = models.CharField(max_length=20, help_text='The Nickname of the Club.')

    def __str__(self):
        return self.name

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club;
        fields = ['name', 'club_nickname', 'year_formed', 'president_name', 'email', 'phone_number'];

#Team Models
class Team(models.Model):
    name = models.CharField("team",max_length=50)
    about = models.CharField(max_length=500)
    training_time = models.CharField(max_length=100)
    club = models.ForeignKey(Club)

    def __str__(self):
        return self.name + " - " + self.club.name

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team;
        fields = ['name', 'about', 'training_time', 'club'];

#Player Models
class Player(models.Model):
    captain_name = models.CharField("captain",max_length=25)
    position = models.CharField(max_length=10)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.name

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player;
        fields = ['captain_name', 'position', 'team'];