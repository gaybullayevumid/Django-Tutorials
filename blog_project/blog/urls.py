# from .views import blogListView, blogDetailView
from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    # path("", blogListView, name="blog_list_view"),
    # path("blogs/<int:id>/", blogDetailView, name="blog_detail_view"),
    path("", BlogListView.as_view(), name="blog_list_view"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog_detail_view"),
]