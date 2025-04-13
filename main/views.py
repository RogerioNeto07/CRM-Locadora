from django.shortcuts import render
from main.models import *
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import JogoForm, PedidoForm, JogoEditForm

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

class RegistarPedido(CreateView):
    template_name = 'registrarpedido.html'
    model = Pedido
    form_class = PedidoForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.valor = 0
        self.object.save()
        form.instance = self.object
        form.save_m2m()
        total = 0
        for jogo in self.object.jogos.all():
            if jogo.estoque > 0:
                jogo.estoque -= 1
                jogo.save()
                total += jogo.preço
        self.object.valor = total
        self.object.save(update_fields=['valor'])
        return super().form_valid(form)
    
class Pedidos(ListView):
    template_name = 'pedidos.html'
    model = Pedido
    context_object_name = 'pedidos'
    ordering = ['-data']

class EditarJogo(UpdateView):
    model = Jogo
    form_class = JogoEditForm
    template_name = 'editar_jogo.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.cleaned_data['estoque'] < 0:
            form.add_error('estoque', 'o estoque não pode ser negativo')
            return self.form_invalid(form)
        return super().form_valid(form)

