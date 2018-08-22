from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import views

router = routers.DefaultRouter()
router.register(r'campus', views.CampusViewSet)

schema_view = get_swagger_view(title='Campus API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
]