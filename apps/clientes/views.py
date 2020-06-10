from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    fields = '__all__'
    context_object_name = 'clientes'
    template_name = 'clientes/cliente_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Cliente.objects.filter(empresa=empresa_logada)


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    fields = '__all__'


class ClienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ['razao_social', 'tipo_participante', 'nome_fantasia', 'fisica_juridica', 'cnpj_cpf', 'inscricao_estadual',
              'inscricao_municipal', 'codigo', 'vendedor', 'endereco', 'complemento', 'numero', 'bairro', 'cidade',
              'cep', 'estado', 'pais', 'telefone', 'celular', 'email', ]

    # success_message = 'O Cliente %(razao_social)s foi criado com sucesso.'

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.empresa = self.request.user.funcionario.empresa
        cliente.save()
        return super(ClienteCreateView, self).form_valid(form)


class ClienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = ['razao_social', 'tipo_participante', 'nome_fantasia', 'fisica_juridica', 'cnpj_cpf', 'inscricao_estadual',
              'inscricao_municipal', 'codigo', 'vendedor', 'endereco', 'complemento', 'numero', 'bairro', 'cidade',
              'cep', 'estado', 'pais', 'telefone', 'celular', 'email', ]

    success_message = 'O Cliente %(razao_social)s foi atualizado com sucesso.'


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    pass
