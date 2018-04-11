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
        form.save();
        return HttpResponseRedirect('/clubs');

def clubs(request):
    clubs = Club.objects.all();
    return render_to_response('app/clubs.html', { 'clubs': clubs });

def clubdetails(request, id):
    club = Club.objects.get(pk = id);
    print('this is the instance of  CLUB  %s' % club)
    return render_to_response('app/clubdetails.html', { 'club': club });

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
