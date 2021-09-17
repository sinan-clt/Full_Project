from os import name
from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=20)
    dob=models.DateField()
    mobile_number=models.IntegerField()
    

class registersecondtable(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    location=models.CharField(max_length=20)
    user_id=models.ForeignKey(register,on_delete=models.CASCADE)


# //////dbconnection/////

class userregister(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    gender=models.CharField(max_length=6)


class students(models.Model):
    firstname=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    dob=models.DateField()


# \\\\todo//////

class doctors(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    department=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)


# \\\\file\\\\

class upload(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    image=models.CharField(max_length=300)


# \\\\AJAX\\\\

class ajaxx(models.Model):
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=20)
    email=models.CharField(max_length=20)