from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def studentapi(request,id=None):
    print(id)
    if request.method == "GET":   
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        return Response(serializer.errors)    

    if request.method == "PUT":
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)