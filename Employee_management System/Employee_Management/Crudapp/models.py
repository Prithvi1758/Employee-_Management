from django.db import models

# Create your models here.
class Student(models.Model):
    Roll_no=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=30,unique=True)
    Department=models.CharField(max_length=100)
    
    class Meta:
        db_table='Student_details'