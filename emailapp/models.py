from django.db import models

# Create your models here.
class stud(models.Model):
    studentid=models.IntegerField()
    studentname=models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    email=models.EmailField() 
    
