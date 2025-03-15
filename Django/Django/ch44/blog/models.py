from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE , primary_key=True)
    page_name = models.CharField(max_length=50   )
    page_cat = models.CharField(max_length=50)
