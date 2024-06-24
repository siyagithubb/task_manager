from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task objects.

    Fields:
        title (CharField): Title or name of the task.
        description (TextField): Detailed description of the task.
        completed (BooleanField): Indicates if the task is completed or not.

    Meta:
        model (Task): Specifies the model to use for the form.
        fields (list): List of fields to include in the form.

    Usage:
        Use this form in views to handle creation and updating of Task objects.
    """

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
