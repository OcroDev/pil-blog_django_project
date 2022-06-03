from django.shortcuts import render
from .models import Post

# Create your views here.

def blog_view(request):
    post = Post.objects.all()
    data = {
        'posts': post ,
    }
    return render (request, "blog_app/blog.html", data)