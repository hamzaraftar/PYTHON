from django.contrib import admin
from django.urls import path
from vege.views import home
from vege.views import delete
from vege.views import update
from vege.views import login
from vege.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('repo/<id>/', delete),
    path('update/<id>/', update),
    path('login/', login),
    path('signup/', register),
]
