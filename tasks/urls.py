from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    """
    List of URL patterns for the project.

    URL Patterns:
        admin/ : Django admin interface.
        '' : Include URLs from the 'tasks' app.
        Add other app URLs here if needed.
    """
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include task app URLs
    # Add other app URLs here if needed
]