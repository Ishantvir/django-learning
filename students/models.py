from django.db import models

# Create your models here.
class Student(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age =  models.IntegerField()
    course = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    marks = models.IntegerField()
    city = models.CharField(max_length=100)