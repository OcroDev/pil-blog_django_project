from django.urls import path
from .views import Registro, cerrar_sesion, iniciar_sesion

urlpatterns = [
    path('', Registro.as_view(), name='registro'),
    path('logout', cerrar_sesion, name='logout'),
    path('login', iniciar_sesion, name='login'),
]
