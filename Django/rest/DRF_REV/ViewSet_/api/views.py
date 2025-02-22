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