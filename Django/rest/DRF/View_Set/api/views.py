from .models import Student
from .serializers import StudentSerializer
from  rest_framework import viewsets
from rest_framework.response import Response

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serizlier = StudentSerializer(stu, many=True)
        return Response(serizlier.data)

    def retrieve(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serizler = StudentSerializer(stu)
        return Response(serizler.data)
 
    def create(self, request):
        serizler = StudentSerializer(data=request.data)
        if serizler.is_valid():
            serizler.save()
            return Response({'msg':'Data Created'}, status=201)
        return Response(serizler.errors)
        
    def update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serizler = StudentSerializer(stu, data=request.data)
        if serizler.is_valid():
            serizler.save()
            return Response({'msg':'Data Updated'})
        return Response(serizler.errors)

    def partial_update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serizler = StudentSerializer(stu , data=request.data, partial=True)
        if serizler.is_valid():
            serizler.save()
            return Response({'msg':'Data Updated'})
        return Response(serizler.errors)

    def destroy(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Data Deleted'})
