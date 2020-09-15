from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from cliente.models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer



    
