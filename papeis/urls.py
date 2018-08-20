from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import views

router = routers.DefaultRouter()
router.register(r'papeis', views.PapelViewSet)

schema_view = get_swagger_view(title='Papeis API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
    # path('', views.index, name='index'),
    # url(r'^api-v1/', include(router.urls, 'papeis')),
    # url(r'^api-v1/', include('rest_framework.urls', namespace='rest_framework'))
]