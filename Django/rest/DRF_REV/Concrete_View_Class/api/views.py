from .serializers import StudentSerializer
from .models import Student

from rest_framework.generics import ListAPIView,CreateAPIView ,RetrieveAPIView

class Student(ListAPIView ,CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentApi(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer