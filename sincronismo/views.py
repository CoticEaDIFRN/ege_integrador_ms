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

def find_user_moodle(request):
    if request.method == "GET":
        username = request.GET['username']
        model = MoodleWSClient()
        response = model.find_user(username)
        return HttpResponse(response)
    else:
        raise Http404()

def create_course(request):
    if request.method == "POST":
        fullname = request.GET['fullname']
        shortname = request.GET['shortname']
        categoryid = request.GET['categoryid']
        model = MoodleWSClient
        response = model.create_course(fullname, shortname, categoryid)
        return HttpResponse(response)
    else:
        raise Http404()

def find_course(request):
    if request.method == "GET":
        name = request.GET['name']
        model = MoodleWSClient()
        response = model.find_course(name)
        return HttpResponse(response)
    else:
        raise Http404()

def create_category(request):
    if request.method == "POST":
        name = request.GET['name']
        description = request.GET['description']
        model = MoodleWSClient
        response = model.create_category(name, description)
        return HttpResponse(response)
    else:
        raise Http404()

def find_category(request):
    if request.method == "GET":
        name = request.GET['name']
        model = MoodleWSClient()
        response = model.find_category(name)
        return HttpResponse(response)
    else:
        raise Http404()

