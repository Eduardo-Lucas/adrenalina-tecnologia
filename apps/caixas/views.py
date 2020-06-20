from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from apps.caixa.models import Caixa


class CaixaListView(LoginRequiredMixin, ListView):
    model = Caixa
