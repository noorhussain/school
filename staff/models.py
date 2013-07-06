from django.db import models

# Create your models here.

class detail(models.Model):
    staff_name=models.CharField(max_length=20)
    staff_age=models.IntegerField(max_length=3)
    section=models.CharField(max_length=20)
    staff_Idn=models.CharField(max_length=10)
    salary=models.IntegerField(max_length=6)
    
