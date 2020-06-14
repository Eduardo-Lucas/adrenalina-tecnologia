from django.contrib import admin

from apps.pedidos.models import Mesa, PedidoStatus, Pedido

admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(PedidoStatus)
