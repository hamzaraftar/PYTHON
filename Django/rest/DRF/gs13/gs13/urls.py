from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>', views.StudentRetrive.as_view()),
    path('studentcreate/', views.StudentCreate.as_view()),
    path('studentupdate/<int:pk>', views.StudentUpdate.as_view()),
]
