from django.shortcuts import render
from django.http import request

# Create your views here.
def paginaPrincipal(request):
    return render(request, "home.html", {})


def ciudad1(request):
    return render(request, "ciudad1.html", {})


def ciudad2(request):
    return render(request, "ciudad2.html", {})


def ciudad3(request):
    return render(request, "ciudad3.html", {})

