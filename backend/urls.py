from django.urls import path
from backend.views.project_views import requirements, task_per_project, workers

from backend.views.setups import equipment, location, project, task
from .views.auth_views import login, register


urlpatterns =[
    path('user', register, name='user'),
    path('sign-in', login, name='sign-in'),
    path('location', location, name='location'),
    path('project', project, name='project'),
    path('task', task, name='task'),
    path('equipment', equipment, name='equipment'),
    path('task-per-location', task_per_project, name='task-per-location'),
    path('workers', workers, name='workers'),
    path('requirements', requirements, name='requirements'),
]