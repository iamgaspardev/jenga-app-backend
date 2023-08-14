from django.db import models

from backend.models.setups_models import Locations


class TaskPerProject(models.Model):

    location_id = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='location_task_project')
    # task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='task_per_project')
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Adjust max_digits and decimal_places based on your requirements
    onprogress = models.CharField(max_length=100, default='True')

class Workers(models.Model):
    
    full_name = models.CharField(max_length=100)
    location_id = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='location_workers')
    task_id = models.ForeignKey(TaskPerProject, on_delete=models.CASCADE, related_name='workers')
    # days = models.IntegerField(default=0)
    payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    onprogress = models.CharField(max_length=100, default='True')

    def __str__(self):
        return self.full_name

class Requirements(models.Model):
    location_id = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='location_requirements')
    task_id = models.ForeignKey(TaskPerProject, on_delete=models.CASCADE, related_name='task_requirement')
    name = models.CharField(max_length=100)
    # equipment_id = models.ForeignKey(Equipments, on_delete=models.CASCADE, related_name='requirement')
    quantity = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    onprogress = models.CharField(max_length=100, default='True')