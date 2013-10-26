from django.shortcuts import render
from songs.models import Account, Mood, Song, Selection

def home(request):
    return render(request, 'anonimous.html', {
#        'account':   Account.objects.get(pk=1),
#        'song':      Song.objects.get(pk=1),
    })
