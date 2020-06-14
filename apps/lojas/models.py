from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa


class Loja(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, unique=False, blank=True, null=True)
    endereco = models.CharField(max_length=50, default='Rua do Sobe e Desce')
    numero = models.CharField(max_length=10, default='S/N', blank=True, null=True)
    bairro = models.CharField(max_length=50, default='Pituba', blank=True, null=True)
    cidade = models.CharField(max_length=50, default='Salvador', blank=True, null=True)
    uf = models.CharField(max_length=2, default='BA')
    telefone = models.CharField(max_length=50, default='(71) 9 9999-9999', blank=True, null=True)
    cep = models.CharField(max_length=10, default='41000-000', blank=True, null=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse('lojas:loja_list')

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
