from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    dob = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    blog_text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.blog_text)