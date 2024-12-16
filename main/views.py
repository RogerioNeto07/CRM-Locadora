from django.shortcuts import render
from main.models import *

def Index(request):
    jogos = Jogo.objects.all()
    context = {'jogos' : jogos}
    return render (request, 'index.html', context)

def Details(request, jogo_id):
    jogos = Jogo.objects.get(id=jogo_id)
    dlcs = DLC.objects.filter(jogo_id=jogo_id)
    context = {'jogos' : jogos, 'dlcs' : dlcs}
    return render (request, 'details.html', context)
