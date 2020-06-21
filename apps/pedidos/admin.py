from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.pedidos.models import Mesa, PedidoStatus, Pedido, PedidoItem

admin.site.register(Mesa)


@admin.register(PedidoStatus)
class PedidoStatusResource(ImportExportModelAdmin):
    pass


@admin.register(Pedido)
class PedidoResource(ImportExportModelAdmin):
    pass


@admin.register(PedidoItem)
class PedidoItemResource(ImportExportModelAdmin):
    pass
