from django.urls import path

from apps.pedidos.views import *
app_name = 'pedidos'
urlpatterns = [
    path('list', PedidoListView.as_view(), name='pedido_list'),
    path('create', PedidoCreateView.as_view(), name='pedido_create'),
    path('update/<int:pk>', PedidoUpdateView.as_view(), name='pedido_update'),

    path('pedido_pdf/<int:id>', pedidoPDF, name='pedido_pdf'),

]
