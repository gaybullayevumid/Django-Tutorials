from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def blogListView(request):
    blogs = Blog.objects.all()

    context = {
        "blogs":blogs,
    }

    return render(request, 'home.html', context=context)

def blogDetailView(request, id):
    blog = get_object_or_404(Blog, id=id)
    context = {
        "blog":blog,
    }

    return render(request, "blog_detail.html", context=context)