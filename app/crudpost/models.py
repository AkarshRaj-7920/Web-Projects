from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)

    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_posts')
    image = models.ImageField(upload_to = 'post_images/')
    location = models.CharField(max_length = 200, blank = True, null = True, help_text = '[city name], [country name]')
    description = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.title} | by {self.author.username}'
    
    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.id)])
    
