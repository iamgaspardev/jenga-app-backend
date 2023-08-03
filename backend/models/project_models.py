from django.db import models


class TaskPerProject(models.Model):

    project_id = models.TextField()
    location_id = models.TextField()
    task_id = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Adjust max_digits and decimal_places based on your requirements
    onprogress = models.CharField(max_length=100, default='True')

class Workers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location_id = models.TextField()
    task_id = models.TextField()
    days = models.IntegerField(default=0)
    payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    onprogress = models.CharField(max_length=100, default='True')

    def __str__(self):
        return self.first_name

class Requirements(models.Model):
    location_id = models.TextField()
    task_id = models.TextField()
    equipment_id = models.TextField()
    quantity = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    onprogress = models.CharField(max_length=100, default='True')