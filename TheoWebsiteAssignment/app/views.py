"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *;




def clubcreate(request):
    if request.method == "GET":
        form = ClubForm();
        return render(request, 'app/create.html', { 'form':form });
    elif request.method == "POST":
        form = ClubForm(request.POST);
        if form.is_valid():
            form.save();
        else:
            return render(request, 'app/create.html', { 'form':form});
        return HttpResponseRedirect('/clubs');

def clubdelete(request, id):
    item = Club.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/clubs');


def clubs(request):
    clubs = Club.objects.all();
    return render_to_response('app/clubs.html', { 'clubs': clubs });

def clubdetails(request, id):
    club = Club.objects.get(pk = id);
    if request.method == "GET":
        form = ClubForm(instance=club)
        pagedata= { 'club': club, 'edit_form' : form }
        return render(request, 'app/clubdetails.html', pagedata);
    else:
        form = ClubForm(request.POST, instance=club);
        if form.is_valid():
            form.save();
        else:
            pagedata= { 'club': club, 'edit_form' : form }
            return render(request, 'app/clubdetails.html', pagedata);
        return HttpResponseRedirect('/clubs');
        
def teams(request):
    teams = Team.objects.all();
    return render_to_response('app/teams.html', { 'teams': teams });

def teamdetails(request, id):
    team = Team.objects.get(pk = id);
    return render_to_response('app/teamdetails.html', { 'team': team });

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

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

