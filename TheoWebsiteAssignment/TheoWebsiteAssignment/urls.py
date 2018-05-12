"""
Definition of urls for TheoWebsiteAssignment.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:

    url(r'^clubs$', app.views.clubs, name='clubs'),
    url(r'^clubs/create$', app.views.clubcreate, name='clubcreate'),
    url(r'^clubs/(?P<id>\d+)$', app.views.clubdetails, name='clubdetails'),
    url(r'^teams$', app.views.teams, name='teams'),
    url(r'^teams/(?P<id>\d+)$', app.views.teamdetails, name='teamdetails'),
    url(r'^clubs/delete/(?P<id>\d+)$', app.views.clubdelete, name='clubdelete'),

    #url(r'^clubs/(?P<name>[A-Za-z]+)$', app.views.clubdetails, name='artistdetails'),

    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
