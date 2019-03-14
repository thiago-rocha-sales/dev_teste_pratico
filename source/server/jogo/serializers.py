from rest_framework import serializers
from .models import Avaliacao, Jogo, Plataforma


class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ('nome',)


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = ('nome', 'data_lancamento', 'plataforma')


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('jogo', 'user', 'valor')