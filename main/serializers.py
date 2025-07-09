from rest_framework import serializers
from .models import *

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'

class DLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DLC
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    valor = serializers.DecimalField(max_digits= 10, decimal_places=2, read_only= True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        jogos_data = validated_data.pop('jogos', [])
        pedido = Pedido.objects.create(**validated_data)
        pedido.jogos.set(jogos_data)
        total_calculado = sum(jogo.preço for jogo in pedido.jogos.all())
        pedido.valor = total_calculado
        pedido.save()

        return pedido
    
    def update(self, instance, validated_data):
        jogos_data = validated_data.pop('jogos_alugados', None)
        instance = super().update(instance, validated_data)
        if jogos_data is not None:
            instance.jogos_alugados.set(jogos_data)
        total_calculado = sum(jogo.preco for jogo in instance.jogos_alugados.all())
        instance.total = total_calculado
        instance.save()

        return instance


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'