from django_services.api import DjangoServiceAPI, register
from .service import ProductService, PlanService
from .serializers import ProductSerializer, PlanSerializer


class ProductAPI(DjangoServiceAPI):
    serializer_class = ProductSerializer
    service_class = ProductService


class PlanAPI(DjangoServiceAPI):
    serializer_class = PlanSerializer
    service_class = PlanService


register('product', ProductAPI)
register('plan', PlanAPI)

