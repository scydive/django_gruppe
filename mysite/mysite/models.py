from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.IntegerField('year')
    location = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    rented_by = models.CharField(max_length=50, default="none")

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)


class Customer(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    age = models.IntegerField('age')
    booked = models.CharField(max_length=45)
    renting = models.IntegerField(default=0)



def __str__(self):
    return self.make + ' ' + self.carmodel