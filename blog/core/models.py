from django.utils import timezone

from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):

    img = models.ImageField(upload_to='post_images/', default="bg.png")

    title = models.CharField(max_length=256)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title
