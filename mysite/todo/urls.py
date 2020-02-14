from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('showTodo', views.getAll, name='getAll'),\
    path('createTodo', views.createTodo, name='createToDo'),
]