from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)