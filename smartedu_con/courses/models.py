from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.name



class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    person = models.ManyToManyField(User, blank=True, related_name='course_person')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/%Y/%m/%d/', default='courses/CINA.png')
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name