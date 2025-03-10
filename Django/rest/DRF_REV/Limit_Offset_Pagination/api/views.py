from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView


class StudentApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
