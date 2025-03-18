from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    course = models.CharField(max_length=50)
