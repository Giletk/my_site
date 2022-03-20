
from django.contrib import admin
from django.urls import path
from .  import views
urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('todolist', views.todo, name="todo"),
    path('taskcreation', views.create, name="create"),
    path('lolkek', views.lolkek, name="lolkek"),
    path('chess', views.chess, name="chess"),
    path('pricelist', views.pricelist, name='pricelist'),
    path('statistics', views.statistics, name='statistics')
]