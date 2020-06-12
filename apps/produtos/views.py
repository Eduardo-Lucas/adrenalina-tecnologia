from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.produtos.forms import ProdutoForm
from apps.produtos.models import Produto, Categoria


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    fields = '__all__'
    context_object_name = 'produtos'
    template_name = 'produtos/produto_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Produto.objects.filter(empresa=empresa_logada)


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    fields = '__all__'


class ProdutoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    success_message = 'O Produto %(nome)s foi criado com sucesso.'


    def form_valid(self, form):
        produto = form.save(commit=False)
        produto.empresa = self.request.user.funcionario.empresa
        produto.save()
        return super(ProdutoCreateView, self).form_valid(form)


class ProdutoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_message = 'O Produto %(nome)s foi atualizado com sucesso.'


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    pass


class CategoriaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    fields = ['nome', ]


class CategoriaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    context_object_name = 'categoria'
    fields = ['nome', ]
