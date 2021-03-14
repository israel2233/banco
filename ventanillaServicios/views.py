from django.shortcuts import render, HttpResponse

# Create your views here.
def df(request):
    return render(request, 'transacciones.html')