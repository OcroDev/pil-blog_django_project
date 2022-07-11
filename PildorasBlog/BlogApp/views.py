from django.shortcuts import render
from carro_compras.carro import Carro
# Create your views here.


def home_view(request):
    carro = Carro(request)
    return render (request, "app/home.html",)


