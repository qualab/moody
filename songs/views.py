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
        return render(request, 'logged.html', {'mood_id': mood_id})


def set_mood(request, mood_id):
    account = get_account(request)
    account.mood = Mood.objects.get(pk=int(mood_id))
    account.save()
    return None


def popular(request):
    return render(request, 'popular.html', {})
