from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter 

class StudentApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields  = ['city']

