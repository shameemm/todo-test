from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    
class Tasks(models.Model):
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=100, default="active")
    todo = models.ForeignKey(to=Todo, on_delete=models.CASCADE)
    
    
    