from django.urls import path

from backend.views.setups import location, project, task
from .views.auth_views import login, register


urlpatterns =[
    path('user', register, name='user'),
    path('sign-in', login, name='sign-in'),
    path('location', location, name='location'),
    path('project', project, name='project'),
    path('task', task, name='task'),
]