from django.contrib import admin
from main.models import *

class JogoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'empresa', 'preço', 'ano']
    ordering = ['-ano']

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome']

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['nome']

class DLCAdmin(admin.ModelAdmin):
    list_display = ['nome', 'jogo', 'preço', 'ano']
    ordering = ['-ano']

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(DLC, DLCAdmin)
admin.site.register(Jogo, JogoAdmin)

# Register your models here.
