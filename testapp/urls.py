from django.urls import path
from testapp.apps import TestappConfig
from . import views

app_name = TestappConfig.name

urlpatterns = [
    path('', views.home, name="home"), # главная страницая
    path('contacts/', views.feedback, name="contacts"),# имя в браузере\путь до контроллера\имя для шаблонов
    path('teach/', views.teach, name="teach"),
]