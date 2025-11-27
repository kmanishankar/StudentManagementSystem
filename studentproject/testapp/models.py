from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    def __str__(self):
        return self.username
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    roll_number=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    father_name=models.CharField(max_length=40)
    branch=models.CharField(max_length=50)
    year=models.IntegerField()
    attendance=models.IntegerField()
    fees=models.FloatField()
    fee_payment=models.CharField(max_length=10)
    def __str__(self):
        return self.name



