from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# Create your views here.
def TodoList(request):
    tasks = Task.objects.all()
    return render(request, "todo_list.html", {"tasks": tasks})


def appendTask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date_added = request.POST.get("date_added")
        Task.objects.create(title=title, date_added=date_added)
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


def updateTask(request, taskID):
    task = get_object_or_404(Task, id=taskID)
    
    if request.method == "POST":
        new_title = request.POST.get("task")
        task.title = new_title
        task.save()
        return redirect("todo_list")
    
    return render(request, "updateTask.html", {"task": task})