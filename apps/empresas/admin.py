from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.empresas.models import Empresa


@admin.register(Empresa)
class EmpresaResource(ImportExportModelAdmin):
    pass
