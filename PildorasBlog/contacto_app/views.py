from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto_view(request):
    formulario = FormularioContacto()
    context = {
        'form':formulario
    }

    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email = EmailMessage("mensaje desde app DJango", "el usuario con nombre {} con la direcicion {} escribe lo siguiente \n\n{}".format(nombre, email, contenido), "", ["rohermy.ochoa@uedonbosco.com"], reply_to=[email]  )
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
               return redirect("/contacto/?novalido")

    return render(request, 'app/contacto.html', context)


