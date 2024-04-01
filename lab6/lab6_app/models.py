from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name='students')
