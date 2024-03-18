
from django.db import models

class Task(models.Model):
    key = models.CharField(max_length=255, default='')  
    value = models.CharField(max_length=255, default='')  
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.key, self.value
    
