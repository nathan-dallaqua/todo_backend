# todo_api/urls.py
from django.urls import path
from .views import TodoItemListCreateView

urlpatterns = [
    path('todos/', TodoItemListCreateView.as_view(), name='todo-list-create'),
]
