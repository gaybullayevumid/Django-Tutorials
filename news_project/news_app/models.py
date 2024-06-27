from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.


class PublishdManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    # id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.Draft
                                )

    view_count = models.IntegerField(default=0)
    objects = models.Manager()
    published = PublishdManager()

    class Meta:
        ordering = ["-publish_time"]
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])
    

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    message = models.TextField()


    def __str__(self) -> str:
        return self.name
    

class Comment(models.Model):
    news = models.ForeignKey(News,
                                on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='comments')
    body = models.TextField()
    created_time = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"
    
# news1 = News.objects.get(id=5)
# news1.comments.all()