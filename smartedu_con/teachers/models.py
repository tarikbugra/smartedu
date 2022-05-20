from django.db import models
from django.forms import CharField


# Create your models here.
class Teacher(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='teachers/%Y/%m/%d/')
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name