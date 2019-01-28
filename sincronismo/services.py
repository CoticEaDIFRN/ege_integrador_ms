from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DiarioSUAPSerializer
from .models import SuapWSClient


# class DiarioService(ListAPIView):
class DiarioService(APIView):
    # queryset = User.objects.all()
    # serializer_class = DiarioSUAPSerializer
    base_name = 'diarios'
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        cod = request.GET['cod']
        model = SuapWSClient()
        response = model.diarios(cod)
        return Response(response)
        # result = DiarioSUAPSerializer(self.get_queryset(), many=True).data
        # result = SUAPClient().get_diarios(request.user.username).data
        # result = [
        #     {
        #         "codigo": 'xx',
        #         "componente_curricular": {
        #             "codigo": 'xx',
        #             "nome": 'xx'
        #         },
        #         "curso": {
        #             "codigo": 'xx',
        #             "nome": 'xx'
        #         },
        #         "campus": {
        #             "codigo": 'xx',
        #             "nome": 'xx',
        #             "sigla": 'xx'
        #         },
        #         "oferta": {
        #             "ano": 'xx',
        #             "periodo": 'xx'
        #         },
        #         "turma": {
        #             "codigo": 'xx',
        #             "nome": 'xx'
        #         }
        #     },
        #     {
        #         "codigo": 'xx',
        #         "componente_curricular_codigo": 'xx',
        #         "componente_curricular_nome": 'xx',
        #         "curso_codigo": 'xx',
        #         "curso_nome": 'xx',
        #         "campus_codigo": 'xx',
        #         "campus_nome": 'xx',
        #         "campus_sigla": 'xx',
        #         "oferta_ano": 'xx',
        #         "oferta_periodo": 'xx',
        #         "turma_codigo": 'xx',
        #         "turma_nome": 'xx'
        #     }
        # ]
        # return Response(result)

    @classmethod
    def get_extra_actions(cls):
        return []


class EscolherService(APIView):
    base_name = 'diarios'
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = [
            {
                "codigo": 'xx',
                "componente_curricular": {
                    "codigo": 'xx',
                    "nome": 'xx'
                },
                "curso": {
                    "codigo": 'xx',
                    "nome": 'xx'
                },
                "campus": {
                    "codigo": 'xx',
                    "nome": 'xx',
                    "sigla": 'xx'
                },
                "oferta": {
                    "ano": 'xx',
                    "periodo": 'xx'
                },
                "turma": {
                    "codigo": 'xx',
                    "nome": 'xx'
                },
                "professores": [
                    {
                        "...": '...'
                    }
                ],
                "alunos": [
                    {
                        "...": '...'
                    }
                ],

            }
        ]
        return Response(result)

    @classmethod
    def get_extra_actions(cls):
        return []


class ConfirmarService(APIView):
    base_name = 'diarios'
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = [
            {
                "codigo": 'xx',
                "componente_curricular": {
                    "codigo": 'xx',
                    "nome": 'xx'
                },
                "curso": {
                    "codigo": 'xx',
                    "nome": 'xx'
                },
                "campus": {
                    "codigo": 'xx',
                    "nome": 'xx',
                    "sigla": 'xx'
                },
                "oferta": {
                    "ano": 'xx',
                    "periodo": 'xx'
                },
                "turma": {
                    "codigo": 'xx',
                    "nome": 'xx'
                },
                "professores": [
                    {
                        "...": '...'
                    }
                ],
                "alunos": [
                    {
                        "...": '...'
                    }
                ],

            }
        ]
        return Response(result)

    @classmethod
    def get_extra_actions(cls):
        return []


class SincronizarService(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = []
        return Response(result)

    @classmethod
    def get_extra_actions(cls):
        return []