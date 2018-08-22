from campus.models import Campus
from rest_framework import serializers

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campus
        fields = ('codigo_moodle','codigo_suap','nome_campus')