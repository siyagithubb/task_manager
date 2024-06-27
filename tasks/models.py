from django.db import models

class Task(models.Model):
    """
    Model representing a Task.

    Attributes:
        title (str): The title or name of the task.
        description (str): Detailed description of the task.
        completed (bool): Indicates if the task is completed or not.

    Methods:
        __str__(): Returns the title of the task for display purposes.
    """

    title = models.CharField(max_length=200, help_text='Enter the title of the task')
    description = models.TextField(help_text='Enter a detailed description of the task')
    completed = models.BooleanField(default=False, help_text='Check if the task is completed')

    def __str__(self):
        """
        String representation of the Task object.

        Returns:
            str: The title of the task.
        """
        return self.title
