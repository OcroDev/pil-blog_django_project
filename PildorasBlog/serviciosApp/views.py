from django.shortcuts import render
from serviciosApp.models import Servicios

# Create your views here.


def servicios_view(request):
    servicio = Servicios.objects.all()
    context = {
        'servicios' : servicio,
    }
    return render (request, "app_servicios/servicios.html", context)
