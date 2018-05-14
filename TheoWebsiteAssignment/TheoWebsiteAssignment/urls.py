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
    # Club url:
    url(r'^clubs$', app.views.clubs, name='clubs'),
    url(r'^clubs/create$', app.views.clubcreate, name='clubcreate'),
    url(r'^clubs/(?P<id>\d+)$', app.views.clubdetails, name='clubdetails'),
    url(r'^clubs/delete/(?P<id>\d+)$', app.views.clubdelete, name='clubdelete'),

    #Team url:
    url(r'^teams$', app.views.teams, name='teams'),
    url(r'^teams/create$', app.views.teamcreate, name='teamcreate'),
    url(r'^teams/(?P<id>\d+)$', app.views.teamdetails, name='teamdetails'),
    url(r'^teams/delete/(?P<id>\d+)$', app.views.teamdelete, name='teamdelete'),

    #Player url:
    url(r'^players$', app.views.players, name='players'),
    url(r'^players/create$', app.views.playercreate, name='playercreate'),
    url(r'^players/(?P<id>\d+)$', app.views.playerdetails, name='playerdetails'),
    url(r'^players/delete/(?P<id>\d+)$', app.views.playerdelete, name='playerdelete'),

    #Generic url
    url(r'^$', app.views.home, name='home'),
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
