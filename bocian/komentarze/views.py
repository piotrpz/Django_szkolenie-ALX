from django.shortcuts import render
from datetime import datetime

# Create your views here.

from django.http import HttpResponse
from komentarze.models import Komentarze

def dodaj(request):
    nick = request.POST['nick']
    email = request.POST['email']
    tytul = request.POST['tytul']
    tresc = request.POST['tresc']
    data = datetime.now()
    komentarz = Komentarze(nick=nick,email=email,tytul=tytul,tresc=tresc, data=data)
    komentarz.save()
    return HttpResponse('dodane')