from django.urls import path
from . import views
urlpatterns = [
    path('', views.servicios_view, name='servicios'),

]
