from django.db import models
from django.contrib.auth.models import User


# Resturent Managment system
# Resturent Model
# User Model
# Rating Model

class Resturent(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.rating
