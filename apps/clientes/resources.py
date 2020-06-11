from import_export import resources

from apps.clientes.models import Cliente


class ClienteResource(resources.ModelResource):
    """
    Permite que eu faça import ou export da class sem precisar estar
    no módulo Admin
    """
    class Meta:
        model = Cliente
        fields = '__all__'
