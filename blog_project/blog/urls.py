from .views import blogListView, blogDetailView
from django.urls import path

urlpatterns = [
    path("", blogListView, name="blog_list_view"),
    path("blogs/<int:id>/", blogDetailView, name="blog_detail_view"),
]