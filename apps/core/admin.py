from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.core.models import Servico, Categoria, Portifolio

admin.site.register(Servico)
admin.site.register(Categoria)


@admin.register(Portifolio)
class PortifolioResource(ImportExportModelAdmin):
    pass
