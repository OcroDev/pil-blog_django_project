from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda_view(request):
    producto = Producto.objects.all()

    context={
        "productos": producto
    }
    return render (request, "app/tienda.html", context)