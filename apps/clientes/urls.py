from django.urls import path
from apps.clientes.views import *
app_name = 'clientes'
urlpatterns = [
    path('list/', ClienteListView.as_view(), name='cliente_list'),
    path('create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('detail/<pk>', ClienteDetailView.as_view(), name='cliente_detail'),
    path('update/<pk>', ClienteUpdateView.as_view(), name='cliente_update'),
    path('delete/<pk>', ClienteDeleteView.as_view(), name='cliente_delete'),
]
