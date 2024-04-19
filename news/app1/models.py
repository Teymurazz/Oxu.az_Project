from django.db import models

class News(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField(max_length=5000, null=True)
    published_at = models.DateTimeField(auto_now_add=True, null=True)
    image_url = models.URLField(max_length=256, null=True)
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.image_url}"

