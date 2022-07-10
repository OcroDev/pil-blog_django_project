from django.urls import path
from . import views
urlpatterns = [
    path('', views.autenticacion_view, name='autenticacion'),
]
