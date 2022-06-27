from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def blog_view(request):
    post = Post.objects.all()
    data = {
        'posts': post ,
    }
    return render (request, "blog_app/blog.html", data)

def categoria(request, id):
    categorias = Categoria.objects.get(id=id)
    post=Post.objects.filter(categoria = categorias)
    data = {
        'categorias' : categorias, 
        'posts': post,
    }
    return render(request, "blog_app/categorias.html", data)