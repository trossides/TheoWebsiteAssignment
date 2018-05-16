"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *;

#Club views
def clubcreate(request):
    if request.method == "GET":
        form = ClubForm();
        return render(request, 'app/create.html', { 'form':form, 'title':'Club Page', 'year':datetime.now().year });
    elif request.method == "POST":
        form = ClubForm(request.POST);
        if form.is_valid():
            form.save();
        else:
            return render(request, 'app/create.html', { 'form':form, 'title':'Club Page', 'year':datetime.now().year});
        return HttpResponseRedirect('/clubs');

def clubdelete(request, id):
    item = Club.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/clubs');

def clubs(request):
    clubs = Club.objects.all();
    return render_to_response('app/clubs.html', { 'clubs': clubs, 'title':'Club Page', 'year':datetime.now().year });

def clubdetails(request, id):
    club = Club.objects.get(pk = id);
    if request.method == "GET":
        form = ClubForm(instance=club)
        pagedata= { 'club': club, 'edit_form' : form, 'title':'Club Page', 'year':datetime.now().year }
        return render(request, 'app/clubdetails.html', pagedata);
    else:
        form = ClubForm(request.POST, instance=club);
        if form.is_valid():
            form.save();
        else:
            pagedata= { 'club': club, 'edit_form' : form, 'title':'Club Page', 'year':datetime.now().year }
            return render(request, 'app/clubdetails.html', pagedata);
        return HttpResponseRedirect('/clubs');

#Team views
def teamcreate(request):
    if request.method == "GET":
        form = TeamForm();
        return render(request, 'app/create.html', { 'form':form, 'title':'Team Page', 'year':datetime.now().year });
    elif request.method == "POST":
        form = TeamForm(request.POST);
        if form.is_valid():
            form.save();
        else:
            return render(request, 'app/create.html', { 'form':form, 'title':'Team Page', 'year':datetime.now().year});
        return HttpResponseRedirect('/teams');

def teamdelete(request, id):
    item = Team.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/teams');

def teams(request):
    teams = Team.objects.all();
    return render_to_response('app/teams.html', { 'teams': teams, 'title':'Team Page', 'year':datetime.now().year});

def teamdetails(request, id):
    team = Team.objects.get(pk = id);
    if request.method == "GET":
        form = TeamForm(instance=team)
        pagedata= { 'team': team, 'team_form' : form, 'title':'Team Page', 'year':datetime.now().year }
        return render(request,'app/teamdetails.html', pagedata);
    else:
        form = TeamForm(request.POST, instance=team);
        if form.is_valid():
            form.save();
        else:
            pagedata= { 'team': team, 'team_form' : form, 'title':'Team Page', 'year':datetime.now().year }
            return render(request, 'app/teamdetails.html', pagedata);
        return HttpResponseRedirect('/teams');
        
#Player views
def playercreate(request):
    if request.method == "GET":
        form = PlayerForm();
        return render(request, 'app/create.html', { 'form':form, 'title':'Captain Page', 'year':datetime.now().year});
    elif request.method == "POST":
        form = PlayerForm(request.POST);
        if form.is_valid():
            form.save();
        else:
            return render(request, 'app/create.html', { 'form':form, 'title':'Captain Page', 'year':datetime.now().year});
        return HttpResponseRedirect('/players');

def playerdelete(request, id):
    item = Player.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/players');

def players(request):
    players = Player.objects.all();
    return render_to_response('app/players.html', { 'players': players, 'title':'Captain Page', 'year':datetime.now().year});

def playerdetails(request, id):
    player = Player.objects.get(pk = id);
    if request.method == "GET":
        form = PlayerForm(instance=player)
        pagedata= { 'player': player, 'player_form' : form, 'title':'Captain Page', 'year':datetime.now().year }
        return render(request, 'app/playerdetails.html', pagedata);
    else:
        form = PlayerForm(request.POST, instance=player);
        if form.is_valid():
            form.save();
        else:
            pagedata= { 'player': player, 'player_form' : form }
            return render(request, 'app/playerdetails.html', pagedata, {'title':'Captain Page', 'year':datetime.now().year});
        return HttpResponseRedirect('/players');

#Generic views
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
