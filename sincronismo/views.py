from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import MoodleWSClient


def create_user_moodle(request):
    if request.method == "POST":
        username = request.GET['username']
        password = request.GET['password']
        firstname = request.GET['firstname']
        lastname = request.GET['lastname']
        email = request.GET['email']

        model = MoodleWSClient()
        response = model.create_user(username, password, firstname, lastname, email)
        return HttpResponse(response)
    else:
        raise Http404()