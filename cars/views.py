from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Branch, Employees, Car
from .serializer import EmployeeSerializer, BranchSerializer, CarSerializer
from django.shortcuts import get_object_or_404

# @api_view(['GET'])
# def customfilter(request):
#     filterpost = Post.objects.filter(name_contains="S").filter(name_contains="1")
#     serializer = PostSerializer(filterpost, many = True)
#     return Response(serializer.data)

@api_view(['GET', 'POST'])
def branch(request):
    if request.method == "GET":
        branch = Branch.objects.all()
        serializer = BranchSerializer(branch, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def branchDetail(request, pk):
    if request.method == "GET":
        branch = get_object_or_404(Branch, id=pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)
    elif request.method == "PUT":
        car = get_object_or_404(Branch, id=pk)
        serializer = BranchSerializer(car, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        car = get_object_or_404(Branch, id=pk)
        car.delete()
        return Response(status=204)