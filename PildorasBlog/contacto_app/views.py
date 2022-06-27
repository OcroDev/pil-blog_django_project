from django.shortcuts import render
from .forms import FormularioContacto
# Create your views here.

def contacto_view(request):
    formulario = FormularioContacto()
    data = {
        'formulario':formulario
    }
    return render(request, 'app/contacto.html', data)

