from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


class StudentAPI(APIView):
    def get(self,request,id):
        try:
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
            
        except:
            return Response(serializer.error)

    def post(self,request):
        try:
            if request.method == "POST":            
                serializer = StudentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)

                return Response(serializer.errors)
    
        except Exception as e:
            return Response({"error": str(e)})  














    
@api_view(["POST"])
def create_student(request):
     

        
@api_view(["PUT"])
def update_student(request,id):
    try:
        if request.method == "PUT":  
            stu = Student.objects.get(id=id)          
            serializer = StudentSerializer(stu , data=request.data ,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors)
    
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