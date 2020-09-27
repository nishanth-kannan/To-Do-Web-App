from django.db import models
from django.db.models import Model

# Create your models here.

#model for a list of tasks and their completion status
class List(Model):
    item = models.CharField(max_length = 200)
    completed = models.BooleanField(default = 'False')

def __str__(self):
    return self.item + ' | ' + str(self.completed) 
