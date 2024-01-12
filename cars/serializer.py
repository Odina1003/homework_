from rest_framework import serializers
from .models import Branch, Car, Employees

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=('id','name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('prof','name', 'branch_id')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=('name', 'price', 'color', 'branch_id')