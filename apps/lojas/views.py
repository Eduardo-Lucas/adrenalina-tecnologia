from django.shortcuts import render
from django.views.generic import ListView

from apps.lojas.models import Loja


class LojaListView(ListView):
    model = Loja
    fields = '__all__'
