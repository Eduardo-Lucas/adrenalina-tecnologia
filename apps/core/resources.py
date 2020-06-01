from import_export import resources

from apps.core.models import Portifolio


class PortifolioResource(resources.ModelResource):

    class Meta:
        model = Portifolio
        fields = '__all__'
