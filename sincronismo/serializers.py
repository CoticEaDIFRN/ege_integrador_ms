from rest_framework.serializers import Serializer, CharField


class CodigoNomeSerializer(Serializer):
    codigo = CharField(label="Código", help_text="")
    nome = CharField(label="Nome")


class ComponenteSerializer(CodigoNomeSerializer):
    pass


class CursoSerializer(CodigoNomeSerializer):
    pass


class CampusSerializer(CodigoNomeSerializer):
    sigla = CharField(label="Sigla")


class TurmaSerializer(CodigoNomeSerializer):
    pass


class OfertaSerializer(Serializer):
    ano = CharField(label="Ano")
    periodo = CharField(label="Período")

 
class DiarioSUAPSerializer(Serializer):
    codigo = CharField(label="Código", help_text="")

    """

    ```
    [
      {
        "codigo": 'xx',
        "componente_curricular": {"codigo": 'xx', "nome": 'xx'},
        "curso": {"codigo": 'xx', "nome": 'xx'},
        "campus": {"codigo": 'xx', "nome": 'xx', "sigla": 'xx'},
        "oferta": {"ano": 'xx',"periodo": 'xx'},
        "turma": {"codigo": 'xx', "nome": 'xx'}
      },
      {
        "codigo": 'xx',
        "componente_curricular_codigo": 'xx',
        "componente_curricular_nome": 'xx',
        "curso_codigo": 'xx',
        "curso_nome": 'xx',
        "campus_codigo": 'xx',
        "campus_nome": 'xx',
        "campus_sigla": 'xx',
        "oferta_ano": 'xx',
        "oferta_periodo": 'xx',
        "turma_codigo": 'xx',
        "turma_nome": 'xx'
      }
    ]
    ```
    """
