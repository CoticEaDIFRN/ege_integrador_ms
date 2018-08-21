from django.shortcuts import render

from papeis.models import Papel
from rest_framework import viewsets, mixins
from papeis.serializers import PapelSerializer


# mixins.CreateModelMixin, 
# mixins.RetrieveModelMixin, # retorna unico registro
# mixins.UpdateModelMixin,
# mixins.DestroyModelMixin,
# mixins.ListModelMixin, # retorna lista
# viewsets.GenericViewSet
class PapelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    list:
    Retorna uma lista com todos os papeis existentes.

    retrieve:
    Retorna um resitro de papeis existentes.
    """
    queryset = Papel.objects.all()
    serializer_class = PapelSerializer
