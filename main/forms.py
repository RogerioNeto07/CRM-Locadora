from django import forms
from .models import Jogo

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = [
            'nome', 'preço', 'ano', 'empresa', 'plataforma', 'genero'
        ]
        widgets = { 
            'plataforma': forms.CheckboxSelectMultiple(),
            'genero': forms.CheckboxSelectMultiple(),
         }