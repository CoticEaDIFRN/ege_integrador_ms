from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import services

v1 = routers.DefaultRouter()
v1.register(r'campi', services.CampusViewSet)
v1.register(r'cursos', services.CursoViewSet)
v1.register(r'papeis', services.PapelViewSet)

# v2 = routers.DefaultRouter()
# v2.register(r'campi', services.CampusViewSet)
# v2.register(r'cursos', services.CursoViewSet)
# v2.register(r'papeis', services.PapeisViewSet)

# schema_view = get_swagger_view(title='API V1')

urlpatterns = [
    path('cachesuap/api/v1/', include((v1.urls, 'cachesuap_v1'))),
    path('cachesuap/api/docs/', get_swagger_view(title='API V1'))
]


"""
http://host:port/integracao/api/v1/cachesuap/campi
http://host:port/integracao/api/v1/cachesuap/cursos
http://host:port/integracao/api/v1/cachesuap/papeis
http://host:port/integracao/api/v1/sincronismo/diarios
http://host:port/integracao/api/v1/sincronismo/escolher
http://host:port/integracao/api/v1/sincronismo/confirmar
http://host:port/integracao/api/v1/sincronismo/sincronizar




http://host:port/integracao/cachesuap/api/v1/campi
http://host:port/integracao/cachesuap/api/v1/cursos
http://host:port/integracao/cachesuap/api/v1/papeis

http://host:port/integracao/sincronismo/api/v1/diarios
http://host:port/integracao/sincronismo/api/v2/diarios
http://host:port/integracao/sincronismo/api/v2/escolher
http://host:port/integracao/sincronismo/api/v2/confirmar
http://host:port/integracao/sincronismo/api/v2/sincronizar

"""