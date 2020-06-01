from django.db import models
from django.urls import reverse


class Servico(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='images/servicos', blank=True, null=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse('index')


class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Portifolio(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nome_projeto = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='images', default='portfolio/portfolio.png', blank=True, null=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return self.nome_projeto
