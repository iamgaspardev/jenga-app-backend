from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    project_id = models.TextField()


    def __str__(self):
        return self.name

class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_id = models.TextField() 


    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 


    def __str__(self):
        return self.name
    
class Equipments(models.Model):
    task_id = models.TextField()
    name = models.CharField(max_length=100)
    description = models.TextField() 


    def __str__(self):
        return self.name