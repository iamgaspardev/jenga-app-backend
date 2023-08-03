from django.db import models

class Locations(models.Model):
    name = models.TextField()
    description = models.TextField() 
    project_id = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return self.name

class Tasks(models.Model):
    name = models.TextField()
    description = models.TextField()
    project_id = models.TextField() 


    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.TextField()
    description = models.TextField() 


    def __str__(self):
        return self.name
    
class Equipments(models.Model):
    task_id = models.TextField()
    name = models.TextField()
    description = models.TextField() 


    def __str__(self):
        return self.name