from django.contrib import admin
from django.contrib.auth.models import User

from backend.models.project_models import Requirements, TaskPerProject, Workers
from .models.user_models import Users
from .models.setups_models import Equipments, Projects, Tasks , Locations
# Register your models here.
admin.site.register([Users,Locations,Tasks,Projects, Equipments, TaskPerProject, Workers, Requirements])