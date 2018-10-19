from django.http import HttpResponse
from django.views import View
from .models import SuapWSClient

class DiarioView(View):
    def get(self, request, *args, **kwargs):
        cod = request.GET['cod']
        client = SuapWSClient()
        response = client.diarios(cod)
        return HttpResponse(response, content_type='application/json')


class MatriculadoView(View):
    def get(self, request, *args, **kwargs):
        diario = request.GET['diario']
        client = SuapWSClient()
        response = client.matriculados(diario)
        return HttpResponse(response, content_type='application/json')