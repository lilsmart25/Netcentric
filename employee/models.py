from django.db import models

# Create your models here.

class Employee(models.Model):
    sno=models.CharField(max_length=20)
    todo=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    
    
def __str__(self):
    return "%s"  %(self.todo)

class Meta:
    db_table = "todo"
    
