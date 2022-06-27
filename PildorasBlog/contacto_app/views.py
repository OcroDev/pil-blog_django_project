from django.shortcuts import render, redirect
from .forms import FormularioContacto
# Create your views here.

def contacto_view(request):
    formulario = FormularioContacto()
    context = {
        'formulario':formulario
    }

    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            return redirect("/contacto/?valido")

    return render(request, 'app/contacto.html', context)


