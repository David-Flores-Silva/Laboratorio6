from django.shortcuts import render
from django.http import request

# Create your views here.
def paginaPrincipal(request):
    return render(request, "home.html", {})

def ciudad1(request):
    return render(request, "ciudad1.html", {})


