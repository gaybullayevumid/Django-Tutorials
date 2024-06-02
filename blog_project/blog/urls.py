from .views import blogListView
from django.urls import path

urlpatterns = [
    path("", blogListView, name="blog_list_view"),
]