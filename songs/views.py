from django.shortcuts import render
from songs.models import Account, Mood, Song, Selection


def get_account(request):
    if 'vk_id' in request.COOKIES:
        name = request.COOKIES.get('vk_id')
        return Account.objects.get_or_create(name=name)[0]
    else:
        return None


def home(request):
    account = get_account(request)
    if account is None:
        return render(request, 'anonimous.html', {})
    else:
        account = get_account(request)
        mood_id = str(account.mood.pk) if account and account.mood else 'no-mood'
        return render(request, 'recomend.html', {'mood_id': mood_id})


def set_mood(request, mood_id):
    account = get_account(request)
    account.mood = Mood.objects.get(pk=int(mood_id))
    account.save()
    return HttpResponse()

def popular(request):
    account = get_account(request)
    mood_id = str(account.mood.pk) if account and account.mood else 'no-mood'
    return render(request, 'popular.html', {'mood_id': mood_id})

def recomend(request):
    account = get_account(request)
    mood_id = str(account.mood.pk) if account and account.mood else 'no-mood'
    return render(request, 'recomend.html', {'mood_id': mood_id})

def usermusic(request):
    account = get_account(request)
    mood_id = str(account.mood.pk) if account and account.mood else 'no-mood'
    return render(request, 'usermusic.html', {'mood_id': mood_id})

def usermusic(request):
    return render(request, 'lucky.html', {})


def rate(request, song_name, mood_id, rating):
    account = get_account(request)
    song = Song.objects.get(name=request.get('song'))
    mood = Mood.objects.get(pk=request.get('mood'))
    selection = Selection.object.get_or_create(account=account, song=song, mood=mood)
    result = Rating.object.get_or_create(selection=selection, rating=int(rating))
    result.save()
    return HttpResponse()
