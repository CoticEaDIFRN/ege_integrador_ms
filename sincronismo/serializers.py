from sincronismo.BaseWSClient import MoodleWSClient, SuapWSClient
from rest_framework.serializers import Serializer, CharField


class CodigoNomeSerializer(Serializer):
    codigo = CharField(label="Código", help_text="Informe o código")
    nome = CharField(label="Nome", help_text="Informe o nome")


class ComponenteSerializer(CodigoNomeSerializer):
    pass


class CursoSerializer(CodigoNomeSerializer):
    pass


class CampusSerializer(CodigoNomeSerializer):
    sigla = CharField(label="Sigla", help_text="Informe a Sigla")


class TurmaSerializer(CodigoNomeSerializer):
    pass


class OfertaSerializer(Serializer):
    ano = CharField(label="Ano", help_text="Informe o Ano")
    periodo = CharField(label="Período", help_text="Informe o Período")

 
class DiarioSUAPSerializer(Serializer):
    codigo = CharField(label="Código", help_text="Informe o Código")
