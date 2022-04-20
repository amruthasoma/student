from django.db import models

# Create your models here.
class colg(models.Model):
    Stud_name=models.CharField(max_length=255)
    Address=models.CharField(max_length=255)
    Gender=models.CharField(max_length=255)
    Qualification=models.CharField(max_length=255)
    Email=models.EmailField()    
    DOB=models.DateField()

