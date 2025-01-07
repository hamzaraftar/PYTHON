from django.urls import path
from .views import index, counter ,register

urlpatterns = [
    path('', index, name='index'),
    path('counter/', counter, name='counter'),
    path('register/', register, name='counter'),
]