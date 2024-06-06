from django.urls import path
from .views import news_list

urlpatterns = [
    path('news/', news_list, name='all_news_list')
]