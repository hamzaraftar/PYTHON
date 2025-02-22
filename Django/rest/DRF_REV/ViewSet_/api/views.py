from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentApi(viewsets.ViewSet):
    def list(self, request):
        try:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)})

    def retrieve(self,request,pk):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)})
        
    def create(self,request):
        try:
            serializer = StudentSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except  Exception as e:
            return Response({'error':str(e)})

    def update(self,request,pk):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)})

    def partial_update(self,request,pk):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)})

    def destory(self,request,pk):
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
        except   Exception as e:
            return Response({'error':str(e)})  