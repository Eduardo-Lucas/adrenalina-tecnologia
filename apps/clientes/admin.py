from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.clientes.models import Cliente


@admin.register(Cliente)
class ClienteResource(ImportExportModelAdmin):
    pass
