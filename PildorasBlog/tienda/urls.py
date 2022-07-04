from django.urls import path
from . import views
urlpatterns = [
    path('', views.tienda_view, name='tienda'),
]
