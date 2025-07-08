from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.get_data),
    path("student/create/", views.create_student),
    path("student/update/<int:id>/", views.update_student),
    path('student/<int:id>/', views.get_data_by_id),
]
