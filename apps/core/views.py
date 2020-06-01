from django.shortcuts import render

from apps.core.models import Servico, Portifolio


def index(request):
    servicos = Servico.objects.all()
    portfolios = Portifolio.objects.all()

    context = {
        'servicos': servicos,
        'portifolios': portfolios,
    }
    return render(request, 'core/index.html', context)
