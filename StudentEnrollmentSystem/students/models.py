from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    stdcode=models.AutoField(primary_key=True)
    fullName=models.CharField(max_length=16)
    phoneNumber=models.CharField(max_length=16)
    email=models.CharField(max_length=16)
    image=models.ImageField(upload_to='media/')
    state=models.CharField(max_length=16)
    district=models.CharField(max_length=16)

class State(models.Model):
    state=models.CharField(max_length=16,primary_key=True)

class District(models.Model):
    id=models.AutoField(primary_key=True)
    state=models.ForeignKey('State',on_delete=models.CASCADE)
    district=models.CharField(max_length=16)