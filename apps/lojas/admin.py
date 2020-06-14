from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.lojas.models import Loja


@admin.register(Loja)
class LojaResource(ImportExportModelAdmin):
    pass

