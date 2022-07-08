from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Review(models.Model):
    description = models.TextField()

    def __str__(self):
        return f'{self.description}'