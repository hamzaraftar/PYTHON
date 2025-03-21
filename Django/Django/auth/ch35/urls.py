from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up),
    path('login/', views.log_in),
    path('profile/', views.profile_page),
    path('logout/', views.log_out),
]
