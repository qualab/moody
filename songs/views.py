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
        return render(request, 'logged.html', {})

def set_mood(request, mid):
    account = get_account(request)
    return None

