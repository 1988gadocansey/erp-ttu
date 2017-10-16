from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return print(request)
    #return HttpResponse("Hello, world. You're at ERP powered by python3 django.")