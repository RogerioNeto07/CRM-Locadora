from django import forms
from .models import Jogo, Pedido

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = [
            'nome', 'preço', 'ano', 'empresa', 'plataforma', 'genero', 'estoque', 'imagem'
        ]
        widgets = { 
            'plataforma': forms.CheckboxSelectMultiple(),
            'genero': forms.CheckboxSelectMultiple(),
         },

class JogoEditForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = [
            'estoque', 'imagem'
        ]

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'jogos'
        ]
        widgets = { 
            'jogos': forms.CheckboxSelectMultiple(),
         }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jogos'].queryset = Jogo.objects.filter(estoque__gt=0)
