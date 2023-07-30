from django.contrib import admin
from django.contrib.auth.models import User
from .models.user_models import Users
from .models.setups_models import Projects, Tasks , Locations
# Register your models here.
admin.site.register([Users,Locations,Tasks,Projects])