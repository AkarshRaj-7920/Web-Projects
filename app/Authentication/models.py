from enum import unique
import uuid
from django.template.defaultfilters import default
from dataclasses import field
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pic')
    bio = models.TextField(max_length = 500)

    def __str__(self):
        return f'{self.user.username} Profile'