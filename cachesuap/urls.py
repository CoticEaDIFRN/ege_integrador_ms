from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import views
from . import services

v1 = routers.DefaultRouter()
v1.register(r'campi', services.CampusViewSet, base_name='campi')
v1.register(r'cursos', services.CursoViewSet, base_name='cursos')
v1.register(r'papeis', services.PapelViewSet, base_name='papeis')


urlpatterns = [
    path('cachesuap/api/v1/', include((v1.urls, 'cachesuap_v1'))),
    path('cachesuap/api/docs/', get_swagger_view(title='API V1'))
]