from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Plataforma(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_lancamento = models.DateTimeField(null=False, blank=False)
    plataforma = models.ManyToManyField(Plataforma)

    def __str__(self):
        return f"{self.nome}"


class Avaliacao(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    valor = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
