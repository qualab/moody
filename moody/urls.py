from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from songs.models import Account, Mood, Song, Selection
admin.site.register(Account)
admin.site.register(Mood)
admin.site.register(Song)
admin.site.register(Selection)

from settings import MEDIA_ROOT

import songs.views

urlpatterns = patterns('',
    url(r'^$', songs.views.home, name='home'),
    url(r'^mood/(\d+)$', songs.views.set_mood, name='mood'),
    url(r'^rate$', songs.views.rate, name='rate'),
    url(r'^popular/$', songs.views.popular, name='popular'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True }),
)
