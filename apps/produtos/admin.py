from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.produtos.models import Produto


@admin.register(Produto)
class ProdutoResource(ImportExportModelAdmin):
    pass
