from django.urls import path
from apps.produtos.views import *
app_name = 'produtos'
urlpatterns = [
    path('list/', ProdutoListView.as_view(), name='produto_list'),
    path('list/<categoria_slug>', ProdutoListView.as_view(), name='produto_por_categoria'),
    path('create/', ProdutoCreateView.as_view(), name='produto_create'),
    path('detail/<pk>/<slug>', ProdutoDetailView.as_view(), name='produto_detail'),
    path('update/<pk>', ProdutoUpdateView.as_view(), name='produto_update'),
    path('delete/<pk>', ProdutoDeleteView.as_view(), name='produto_delete'),

    path('create_cat/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('update_cat/<pk>', CategoriaUpdateView.as_view(), name='categoria_update'),

]
