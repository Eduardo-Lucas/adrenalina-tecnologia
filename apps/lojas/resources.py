from import_export import resources

from apps.lojas.models import Loja


class LojaResource(resources.ModelResource):

    class Meta:
        model = Loja
        fields = '__all__'
