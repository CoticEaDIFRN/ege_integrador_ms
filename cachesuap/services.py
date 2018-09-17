from django.shortcuts import render

from rest_framework import viewsets, mixins

from .models import Campus
from .models import Papel
from .models import Curso

from .serializers import CampusSerializer
from .serializers import PapelSerializer
from .serializers import CursoSerializer


# mixins.CreateModelMixin, 
# mixins.RetrieveModelMixin, # retorna unico registro
# mixins.UpdateModelMixin,
# mixins.DestroyModelMixin,
# mixins.ListModelMixin, # retorna lista
# viewsets.GenericViewSet
class CampusViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    list:
    Retorna uma lista com todos os campus existentes.

    retrieve:
    Retorna um resitro de um campus existente.
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class PapelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    list:
    Retorna uma lista com todos os papeis existentes.

    retrieve:
    Retorna um resitro de um papel existente.
    """
    queryset = Papel.objects.all()
    serializer_class = PapelSerializer


class CursoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    list:
    Retorna uma lista com todos os cursos existentes.

    retrieve:
    Retorna um resitro de um curso curso existente.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
