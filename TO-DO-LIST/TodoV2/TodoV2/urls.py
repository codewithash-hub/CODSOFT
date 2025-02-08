from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.TodoList, name="todo_list"),
    path("append", views.appendTask, name="appendTask"),
    path("delete/<int:taskID>/", views.deleteTask, name="deleteTask"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle_task"),
    path("update/<int:taskID>/", views.updateTask, name="updateTask")
]
