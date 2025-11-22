from django.db import models
class Details(models.Model):
    roomno=models.IntegerField()
    name=models.CharField(max_length=30)
    fees=models.IntegerField()
    address=models.CharField(max_length=30)
# Create your models here.
