from django.db import models

# Create your models here.

from django.db import models
    
class Users(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __repr__(self):
    #     return f"Movie: {self.title} {self.description} ({self.release_date}) {self.created_at}"