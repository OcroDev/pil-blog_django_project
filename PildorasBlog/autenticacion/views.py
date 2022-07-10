from django.shortcuts import render
from .forms import FormularioLogin
# Create your views here.

def autenticacion_view(request):
    data = {
        'form': FormularioLogin()
    }
    return render (request, "app/autenticacion.html",data)