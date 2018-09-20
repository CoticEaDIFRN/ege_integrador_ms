from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DiarioSUAPSerializer


# class DiarioService(ListAPIView):
class DiarioService(APIView):
    # queryset = User.objects.all()
    # serializer_class = DiarioSUAPSerializer
    base_name = 'diarios'
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # result = DiarioSUAPSerializer(self.get_queryset(), many=True).data
        # result = SUAPClient().get_diarios(request.user.username).data
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
                }
            }
        ]
        return Response(result)

    @classmethod
    def get_extra_actions(cls):
        return []


class EscolherService(APIView):
    base_name = 'escolher'
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
    base_name = 'confirmar'
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
    base_name: 'sincronizar'
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     result = [
    #        {
    #             "codigo": 'xx',
    #             "componente_curricular": {
    #                 "codigo": 'xx',
    #                 "nome": 'xx'
    #             },
    #             "curso": {
    #                 "codigo": 'xx',
    #                 "nome": 'xx'
    #             },
    #             "campus": {
    #                 "codigo": 'xx',
    #                 "nome": 'xx',
    #                 "sigla": 'xx'
    #             },
    #             "oferta": {
    #                 "ano": 'xx',
    #                 "periodo": 'xx'
    #             },
    #             "turma": {
    #                 "codigo": 'xx',
    #                 "nome": 'xx'
    #             }
                
    #         }

    #     ]
    #     return Response(result)

    # @classmethod
    # def get_extra_actions(cls):
    #     return []