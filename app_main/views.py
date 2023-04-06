from rest_framework.viewsets import ModelViewSet
from .models import Entity, Property
from .serializers import EntitySerializer, PropertySerializer


# Create your views here.
class EntityModelViewSet(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class PropertyModelViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
