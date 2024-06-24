from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    """
    Render a list of all tasks.

    Retrieves all Task objects from the database and renders them in a template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML template displaying the list of tasks.
    """
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    """
    Add a new task.

    Handles both GET (initial form display) and POST (form submission) requests.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML template displaying the add task form or redirects to task_list on successful form submission.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def task_detail(request, task_id):
    """
    Display details of a specific task.

    Retrieves a specific Task object based on task_id from the database and renders its details.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to display.

    Returns:
        HttpResponse: Rendered HTML template displaying the details of the specified task.
    """
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def edit_task(request, task_id):
    """
    Edit an existing task.

    Handles both GET (initial form display) and POST (form submission) requests to edit a specific task.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to edit.

    Returns:
        HttpResponse: Rendered HTML template displaying the edit task form or redirects to task_detail on successful form submission.
    """
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})