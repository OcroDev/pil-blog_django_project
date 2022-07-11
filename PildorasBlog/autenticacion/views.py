from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#from .forms import FormularioLogin

# Create your views here.

class Registro(View):
    
    def get(self, request):
        form = UserCreationForm()
        data = {
            "form":form
        }
        return render(request, "app/registro.html",data)
    
    def post(self,request):
        form = UserCreationForm(request.POST)
        data = {
            "form": form
        }
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request,"app/registro.html",data)



def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)       
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            pass_usuario = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = pass_usuario)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "informacion incorrecta")
    form = AuthenticationForm()
    data = {
        'form':form

    }
    return render(request, "app/login.html", data)

#def autenticacion_view(request):
 #   data = {
  #      'form': FormularioLogin()
   # }
    #return render (request, "app/autenticacion.html",data)