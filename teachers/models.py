from django.db import models

# Create your models here.

class Details(models.Model):
    faculty_name=models.CharField(max_length=20)
    faculty_age=models.IntegerField(max_length=3)
    main_subject=models.CharField(max_length=20)
    faculty_Idn=models.CharField(max_length=10)
    salary=models.IntegerField(max_length=6)
    
