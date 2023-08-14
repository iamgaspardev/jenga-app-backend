from django.urls import path
from backend.views.project_views import process_data_view, requirements, task_per_location, workers

from backend.views.setups import equipment, location, location_delete, project, task
from .views.auth_views import login, register


urlpatterns =[
    path('api/user', register, name='user'),
    path('api/sign-in', login, name='sign-in'),
    path('api/locations', location, name='locations'),
    path('api/location/<int:pk>/', location_delete, name='location'),
    path('api/project', project, name='project'),
    path('api/task', task, name='task'),
    path('api/equipment', equipment, name='equipment'),
    path('api/task-per-location', task_per_location, name='task-per-location'),
    path('api/workers', workers, name='workers'),
    path('api/requirements', requirements, name='requirements'),
    path('api/process_data', process_data_view, name='process_data'),
]