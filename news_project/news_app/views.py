from django.shortcuts import render, get_object_or_404
from .models import News, Category

# Create your views here.

def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list":news_list
    }

    return render(request, "news/news_list.html", context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        "news":news
    }

    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news':news,
        'categories':categories
    }

    return render(request, 'news/home.html', context)

def contactPageView(request):
    context = {}
    return render(request, 'news/contact.html', context)