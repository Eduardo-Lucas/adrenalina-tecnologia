from django.urls import path
from .views import *

urlpatterns = [
    path('list', LojaListView.as_view(), name='loja_list'),

]
