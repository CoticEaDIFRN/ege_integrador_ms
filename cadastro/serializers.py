from cadastro.models import Campus
from cadastro.models import Curso
from cadastro.models import Papel

from rest_framework import serializers

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Campus
        fields = ('codigo_moodle','codigo_suap','nome')


class CursoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Curso
        fields = ('codigo_moodle','codigo_suap','nome')


class PapelSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Papel
        fields = ('id', 'codigo_moodle', 'codigo_suap', 'nome')