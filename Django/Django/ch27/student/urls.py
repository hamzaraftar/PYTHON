from django.urls import path,include
from student import views

urlpatterns = [
    path('register/',views.register_student ),
]
