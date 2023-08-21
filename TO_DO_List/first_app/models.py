from django.db import models

# Create your models here.

class Task_Model(models.Model):    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)    
    is_completed = models.BooleanField(default=False)
      
    
