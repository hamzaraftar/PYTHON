
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.get_data),
    path('student/<int:id>/', views.get_data_by_id),
    path('student/create/', views.create_student),
    path('student/update/<int:id>/', views.update_student),
    path('student/delete/<int:id>/', views.delete_student),
]
