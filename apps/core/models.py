from django.db import models
from django.urls import reverse


class Servico(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse('index')
