from rest_framework import serializers
from .models import Avaliacao, Jogo, Plataforma


class PlataformaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plataformas-detail', read_only=True)

    class Meta:
        model = Plataforma
        fields = ('url', 'nome')


class JogoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='jogos-detail', read_only=True)

    plataforma = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='plataformas-detail',
        queryset=Plataforma.objects.all())

    class Meta:
        model = Jogo
        fields = (
            'url',
            'nome', 
            'data_lancamento', 
            'plataforma')


class AvaliacaoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='avaliacaos-detail', read_only=True)

    jogos = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='jogos-detail',
        queryset=Jogo.objects.all())

    class Meta:
        model = Avaliacao
        fields = ('url', 'jogos', 'user', 'valor')