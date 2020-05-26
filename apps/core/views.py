from django.shortcuts import render

from apps.core.models import Servico


def index(request):
    servicos = Servico.objects.all()

    context = {
        'servicos': servicos
    }
    return render(request, 'core/index.html', context)
