from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# Create your views here.
def TodoList(request):
    tasks = Task.objects.all()
    return render(request, "todo_list.html", {"tasks": tasks})


def appendTask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)
        return redirect("todo_list")
    return render(request, "appendTask.html")


def deleteTask(request, taskID):
    task = get_object_or_404(Task, id=taskID)
    task.delete()
    return redirect("todo_list")


def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("todo_list")