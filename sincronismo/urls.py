from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import views
from . import services

v1 = routers.DefaultRouter()
v1.register(r'diarios', services.DiarioService, base_name='diarios')
v1.register(r'escolher', services.EscolherService, base_name='escolher')
v1.register(r'confirmar', services.ConfirmarService, base_name='confirmar')
v1.register(r'sincronizar', services.SincronizarService, base_name='sincronizar')

urlpatterns = [
    path('sincronismo/api/v1/', include((v1.urls, 'sincronismo_v1'))),
    path('sincronismo/api/docs/', get_swagger_view(title='API V1'))
]