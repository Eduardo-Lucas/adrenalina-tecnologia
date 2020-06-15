from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.produtos.models import Categoria, Produto


@admin.register(Categoria)
class CategoriaResource(ImportExportModelAdmin):
    pass


@admin.register(Produto)
class ProdutoResource(ImportExportModelAdmin):
    pass
