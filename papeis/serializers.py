from papeis.models import Papel
from rest_framework import serializers

class PapelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Papel
        fields = ('id', 'codigo_moodle', 'codigo_suap', 'nome')
