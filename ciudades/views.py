from ciudades.models import Ciudad
from django.shortcuts import render
from django.http import request
from .models import Ciudad

# Create your views here.
def paginaPrincipal(request):
    #crearemos objetos de la clase Ciudad
    c1 = Ciudad()
    c1.nombre = "Ciudad Blanca"
    c1.pais = "Peru"
    c1.departamento = "Arequipa"
    c1.oferta = True
    c1.precio = 500

    c2 = Ciudad()
    c2.nombre = "Brasilia"
    c2.pais = "Brasil"
    c2.departamento = "Brasilia"
    c2.oferta = False
    c2.precio = 600

    c3 = Ciudad()
    c3.nombre = "Uruguay"
    c3.pais = "Uruguay"
    c3.departamento = "Montevideo"
    c3.oferta = True
    c3.precio = 700

    return render(request, "home.html", {"c1": c1, "c2": c2, "c3": c3})


def ciudad1(request):
    return render(request, "ciudad1.html", {})


def ciudad2(request):
    return render(request, "ciudad2.html", {})


def ciudad3(request):
    return render(request, "ciudad3.html", {})


def reservar(request):
    return render(request, "reservar.html", {})
