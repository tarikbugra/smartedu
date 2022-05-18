from enum import unique
from tabnanny import verbose
from django.db import models
from django.forms import CharField


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/%Y/%m/%d/', default='courses/CINA.png')
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name