# Generated by Django 5.0.6 on 2024-06-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_remove_news_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=250, null=True),
        ),
    ]