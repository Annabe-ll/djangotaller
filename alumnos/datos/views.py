from django.shortcuts import render
from django.http import HttpResponse


def hola(request):
	return HttpResponse("Hello World desde Django")
# Create your views here.


