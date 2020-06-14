from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from apps.empresas.models import Empresa


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True, db_index=True, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Categoria, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('produto_por_categoria', args=[self.slug])


class Produto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    foto = models.ImageField(upload_to='produtos', default='produtos/product.jpg', blank=True)
    descricao = models.CharField(max_length=500, blank=True)
    preco = models.DecimalField(max_digits=16, decimal_places=2)
    preco_desconto = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    saldo = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        index_together = ('id', 'slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Produto, self).save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.foto.url
        except:
            url = 'img/no_image.png'
        return url

    def __str__(self):
        return self.nome + ' R$ ' + str(self.preco)

    def is_available(self):
        if self.saldo > 0:
            self.disponivel = True
        else:
            self.disponivel = False
        return self.disponivel

    def is_preco_desconto(self):
        if self.preco_desconto:
            return self.preco_desconto
        else:
            return '0,00'

    @staticmethod
    def get_absolute_url():
        return reverse('produtos:produto_list')
