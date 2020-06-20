from django.urls import path

from .views import *
app_name = 'caixa'

urlpatterns = [
    path('list', CaixaListView.as_view(), name='caixa_list'),
]
