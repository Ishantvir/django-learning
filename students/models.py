from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age =  models.IntegerField()
    course = models.CharField(max_length=100)
    address = models.TextField()
    marks = models.IntegerField()
    city = models.CharField(max_length=100)