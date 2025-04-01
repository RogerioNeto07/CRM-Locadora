from django.shortcuts import render
from main.models import *
from django.views.generic import CreateView
from .models import *
from .forms import JogoForm

def Index(request):
    jogos = Jogo.objects.all()
    context = {'jogos' : jogos}
    return render (request, 'index.html', context)

def Details(request, jogo_id):
    jogos = Jogo.objects.get(id=jogo_id)
    dlcs = DLC.objects.filter(jogo_id=jogo_id)
    context = {'jogos' : jogos, 'dlcs' : dlcs}
    return render (request, 'details.html', context)

class Create(CreateView):
    template_name = 'create.html'
    model = Jogo
    form_class = JogoForm
    success_url = '/'

