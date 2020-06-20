from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.core.choices import STATUS_CAIXA_CHOICES, ENTRADA_SAIDA_CHOICES
from apps.financeiro.models import TipoPagamento


class Caixa(models.Model):
    data_movimento = models.DateField(db_index=True)
    data_criacao = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=7, choices=STATUS_CAIXA_CHOICES, default='Aberto')
    valor_inicial = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)

    class Meta:
        ordering = ['-id']
        unique_together = ['data_movimento', 'user']

    def __str__(self):
        return str(self.data_movimento) + ' - ' + str(self.user) + ' - ' + self.status

    @staticmethod
    def get_absolute_url():
        return reverse('caixas:caixa_list')


class CaixaMovimento(models.Model):
    caixa = models.ForeignKey(Caixa, related_name='movimentos', on_delete=models.CASCADE)
    tipopagamento = models.ForeignKey(TipoPagamento, on_delete=models.PROTECT)
    valor_movimento = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    entrada_saida = models.CharField(max_length=1, choices=ENTRADA_SAIDA_CHOICES, default='D')
    observacao = models.CharField(max_length=100, null=True, blank=True)
