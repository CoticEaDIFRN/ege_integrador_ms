from django.shortcuts import render
from rest_framework import viewsets, mixins
from curso.models import Curso
from curso.serializers import CursoSerializer


class CursoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer