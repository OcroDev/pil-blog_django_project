from django.shortcuts import render


# Create your views here.


def home_view(request):
    return render (request, "app/home.html",)

def contacto_view(request):
    return render (request, "app/contacto.html",)


def blog_view(request):
    return render (request, "app/blog.html",)

def tienda_view(request):
    return render (request, "app/tienda.html",)