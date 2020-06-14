from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.financeiro.models import TipoPagamento, PrazoPagamento, TabelaPreco


@admin.register(TipoPagamento)
class TipoPagamentoResource(ImportExportModelAdmin):
    pass


@admin.register(PrazoPagamento)
class PrazoPagamentoResource(ImportExportModelAdmin):
    pass


@admin.register(TabelaPreco)
class TabelaPrecoResource(ImportExportModelAdmin):
    pass
