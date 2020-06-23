from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.core.choices import SIM_NAO_CHOICES
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    """Manutenção do Cadastro de Funcionários"""
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, )
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.PROTECT)
    quantidade_clientes = models.PositiveIntegerField('Qtd Clientes', default=0)
    telefone = models.CharField(max_length=30, null=True, blank=True)
    celular = models.CharField("Celular", max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    ativo = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='Sim')
    endereco = models.CharField("Endereço", max_length=60, blank=True, null=True)
    complemento = models.CharField("Complemento", max_length=60, blank=True, null=True)
    numero = models.CharField("Número", max_length=20, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField("CEP", max_length=9, null=True, blank=True, )
    estado = models.CharField("UF", max_length=2, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True, default='Brasil')



    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse('funcionarios:funcionario_list')
