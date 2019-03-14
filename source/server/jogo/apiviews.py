from rest_framework import viewsets
from .models import Avaliacao, Jogo, Plataforma
from .serializers import JogoSerializer, PlataformaSerializer, AvaliacaoSerializer


class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer