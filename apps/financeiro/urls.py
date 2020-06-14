from django.urls import path
from .views import *

urlpatterns = [
    path('tipolist', TipoPagamentoListView.as_view(), name='tipopagamento_list'),
    path('prazolist', PrazoPagamentoListView.as_view(), name='prazopagamento_list'),
]
