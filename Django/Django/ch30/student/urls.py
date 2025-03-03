from django.urls import path
from student import views
urlpatterns = [
    path("student/" , views.show_form )
]