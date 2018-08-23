from curso.models import Curso
from rest_framework import serializers

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('codigo_moodle','codigo_suap','nome_curso')