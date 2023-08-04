from django.urls import path
from backend.views.project_views import requirements, task_per_project, workers

from backend.views.setups import equipment, location, project, task
from .views.auth_views import login, register


urlpatterns =[
    path('api/user', register, name='user'),
    path('api/sign-in', login, name='sign-in'),
    path('api/location', location, name='location'),
    path('api/project', project, name='project'),
    path('api/task', task, name='task'),
    path('api/equipment', equipment, name='equipment'),
    path('api/task-per-location', task_per_project, name='task-per-location'),
    path('api/workers', workers, name='workers'),
    path('api/requirements', requirements, name='requirements'),
]