from django.urls import path
from .views import index, counter

urlpatterns = [
    path('', index, name='index'),
    path('counter/', counter, name='counter'),
]