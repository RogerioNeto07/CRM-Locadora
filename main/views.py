from django.shortcuts import render
from main.models import *
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import JogoForm, PedidoForm, JogoEditForm
from django.contrib import messages

class Index(ListView):
    template_name = 'index.html'
    model = Jogo
    context_object_name = 'jogos'

class Details(DetailView):
    model = Jogo
    template_name = 'details.html'
    context_object_name = 'jogos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jogo = self.get_object()
        context['dlcs'] = DLC.objects.filter(jogo=jogo)
        return context


# def Details(request, jogo_id):
#     jogos = Jogo.objects.get(id=jogo_id)
#     dlcs = DLC.objects.filter(jogo_id=jogo_id)
#     context = {'jogos' : jogos, 'dlcs' : dlcs}
#     return render (request, 'details.html', context)

class Create(CreateView):
    template_name = 'create.html'
    model = Jogo
    form_class = JogoForm
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Jogo adicionado com sucesso!")
        return response

class RegistarPedido(CreateView):
    template_name = 'registrarpedido.html'
    model = Pedido
    form_class = PedidoForm
    success_url = 'pedidos'

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
        response = super().form_valid(form)
        messages.success(self.request, 'Pedido registrado com sucesso!')
        return response
    
class Pedidos(ListView):
    template_name = 'pedidos.html'
    model = Pedido
    context_object_name = 'pedidos'
    ordering = ['-data']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedidos = context['pedidos']
        context['faturamento'] = sum(pedido.valor for pedido in pedidos)
        return context

class EditarJogo(UpdateView):
    model = Jogo
    form_class = JogoEditForm
    template_name = 'editar_jogo.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.cleaned_data['estoque'] < 0:
            form.add_error('estoque', 'o estoque não pode ser negativo')
            return self.form_invalid(form)
        response = super().form_valid(form)
        messages.success(self.request, 'Jogo editado com sucesso!')
        return response

