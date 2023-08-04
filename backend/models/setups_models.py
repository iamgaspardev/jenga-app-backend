from django.utils import timezone
from django.db import models



class Projects(models.Model):
    project_name = models.TextField()
    project_description = models.TextField() 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name
    
class Locations(models.Model):
    location_name = models.TextField()
    location_description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='locations')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.location_name
    
class Tasks(models.Model):
    task_name = models.TextField()
    task_description = models.TextField()
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task_name
        
class Equipments(models.Model):
    task_id = models.TextField()
    equipment_name = models.TextField()
    equipment_description = models.TextField() 
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='equipments')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.equipment_name