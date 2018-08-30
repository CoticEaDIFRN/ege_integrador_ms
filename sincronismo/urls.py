from django.urls import path

from . import views

urlpatterns = [
    path('moodle/create_user', views.create_user_moodle, name='moodle'),
]