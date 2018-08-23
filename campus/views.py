from django.shortcuts import render
from rest_framework import viewsets, mixins
from campus.models import Campus
from campus.serializers import CampusSerializer


class CampusViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer