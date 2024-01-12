from django.db import models

class Branch(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

class Employees(models.Model):
    prof = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Car(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    color = models.CharField(max_length=30)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)