# Generated by Django 5.0.3 on 2024-04-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_news_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='body',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]