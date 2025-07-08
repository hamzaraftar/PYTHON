from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

@api_view(["GET"])
def get_data(request):
    try:
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)  # Fixed here
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

@api_view(["GET"])
def get_data_by_id(request, id):
    try:
        student = Student.objects.get(id=id)  # Use named argument 'id=id'
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"error": "Student doesn't exist"})
