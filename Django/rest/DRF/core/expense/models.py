from django.db import models

# Create your models here.

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    