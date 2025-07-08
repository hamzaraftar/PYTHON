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


# get student by id 
@api_view(["GET"])
def get_data_by_id(request, id):
    try:
        student = Student.objects.get(id=id)  # Use named argument 'id=id'
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"error": "Student doesn't exist"})

# create student
@api_view(["POST"])
def create_student(request):
    try:
        if request.method == "POST":  
            serializer = StudentSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
    except Exception as e:
        return Response({"error": str(e)})
    
@api_view(["PUT"])  # ✅ Must include "PUT"
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
        serializer = StudentSerializers(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})
    except Exception as e:
        return Response({"error": str(e)})

@api_view(["DELETE"])
def delete_student(request,id):
    try:
        if request.method =="DELETE":
            stu = Student.objects.get(id=id)
            stu.delete()
        return Response("Delete Successfully")
    except:
        return Response({"error":"Data can't Delete "})    