from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def siva(request,name):
    return HttpResponse(f'<center><h2><i>Welcome to Vizag: {name}</i></h2></center>')

