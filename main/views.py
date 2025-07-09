from django.shortcuts import render
from main.models import *
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import JogoForm, PedidoForm, JogoEditForm
from django.contrib import messages
from rest_framework import generics, viewsets
from .serializers import *

# views da aplicação django tradicional

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

class DeletarJogo(DeleteView):
    model = Jogo
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

#views da API
class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class DLCViewSet(viewsets.ModelViewSet):
    queryset = DLC.objects.all()
    serializer_class = DLCSerializer

class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
