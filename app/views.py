from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')
def criando_django(request):
    return render(request, 'criando_django.html')
def fundamentos_csharp(request):
    return render(request,'fundamentos_csharp.html')
def fundamentos_python(request):
    return render(request, 'fundamentos_python.html')
def fundamentos_flutter(request):
    return render(request, 'fundamentos_flutter.html')
