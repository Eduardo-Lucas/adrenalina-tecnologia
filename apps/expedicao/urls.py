from django.urls import path
from .views import *
app_name = 'expedicao'
urlpatterns = [
    path('expedicao/', expedicao, name='expedicao'),
    path('inicia_separacao/(<id>[0-9]+)/', inicia_separacao, name='inicia_separacao'),
    path('finaliza_separacao/(<id>[0-9]+)/', finaliza_separacao, name='finaliza_separacao'),
    path('estorna_separacao/(<id>[0-9]+)/', estorna_separacao, name='estorna_separacao'),
    path('altera_loja/(<pk>[0-9]+)/', AlteraLojaUpdate.as_view(), name='altera_loja'),

]
