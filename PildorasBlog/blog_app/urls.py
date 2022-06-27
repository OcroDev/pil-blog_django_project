from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('categoria/<id>/', views.categoria, name='categorias')
]
