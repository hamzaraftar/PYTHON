from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.setcookie),
    path('get/student/', views.getcookie),
    path('delete/student/', views.delcookie),

]
