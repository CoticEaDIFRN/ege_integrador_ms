from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import services

v1 = DefaultRouter()
v1.register(r'diarios', services.DiarioService, base_name='diarios')
v1.register(r'escolher', services.EscolherService, base_name='escolher')
v1.register(r'confirmar', services.ConfirmarService, base_name='confirmar')
v1.register('/sincronizar/', services.SincronizarService, base_name='sincronizar')

# urlpatterns = [
#     path('integracao/', include([
#         path('moodle/create_user', views.create_user_moodle, name='moodle_create'),
#         path('moodle/update_user', views.update_user_moodle, name='moodle'),
#         path('moodle/find_user', views.find_user_moodle, name='moodle'),
#         path('moodle/create_course', views.create_course, name='moodle'),
#         path('moodle/find_course', views.find_course, name='moodle'),
#         path('moodle/create_category', views.create_category, name='moodle'),
#         path('moodle/find_category', views.find_category, name='moodle'),
#     ])),
#     path('integracao/api/v1', include((v1.urls, 'integracao_v1')))
# ]
