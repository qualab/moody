from django.shortcuts import render, HttpResponse
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

def mood(request):
    account = get_account(request)
    mood_id = str(account.mood.pk) if account and account.mood else 'no-mood'
    return render(request, 'mood.html', {'mood_id': mood_id})

def lucky(request):
    account = get_account(request)
    mood_id = str(account.mood.pk) if account and account.mood else 'no-mood'
    return render(request, 'lucky.html', {'mood_id': mood_id})


def rate(request):
    account = get_account(request)
    song = Song.objects.get_or_create(name=request.GET.get('song'))[0]
    mood = Mood.objects.get(pk=request.GET.get('mood'))
    selection = Selection.objects.get_or_create(account=account, song=song, mood=mood)
    return HttpResponse('{"status": "ok"}')
