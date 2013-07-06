from django.db import models

class details(models.Model):
    Student_name=models.CharField(max_length=20)
    student_class=models.IntegerField(max_length=2)
    main_subjects=models.CharField(max_length=10)
    student_Id_no=models.CharField(max_length=10)
    marks_student=models.IntegerField(max_length=3)
    Average_marks=models.FloatField(max_length=4)
    Fee_student=models.IntegerField(max_length=6)
    
    
