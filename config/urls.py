from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls', namespace='testapp'))#Здесь namespace='catalog' тоже должен совпадать с app_name в testapp/urls.py.
]