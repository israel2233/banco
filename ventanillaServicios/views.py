from django.shortcuts import render, HttpResponse

# Create your views here.
def df(request):
    return HttpResponse('<h1>hola</h1>')