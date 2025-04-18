from django.db import models

class Plataforma(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False)
    preço = models.FloatField(max_length=10, null= False, blank= False)
    ano = models.IntegerField(null= False, blank= False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    plataforma = models.ManyToManyField(Plataforma)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.nome
    
class DLC(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False)
    preço = models.FloatField(max_length=10, null= False, blank= False)
    ano = models.IntegerField(null= False, blank= False)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.nome

