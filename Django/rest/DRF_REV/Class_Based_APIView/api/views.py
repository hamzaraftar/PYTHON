from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


class StudentAPI(APIView):
    def get(self,request,id=None):
        try:
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
            
        except Exception as e:
            return Response({"error": str(e)})

    def post(self,request):
        try:                       
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors)
    
        except Exception as e:
            return Response({"error": str(e)})  

    def put(self,request,id):
       try:            
            stu = Student.objects.get(id=id)          
            serializer = StudentSerializer(stu , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors)
       
       except Exception as e:
            return Response({"error": str(e)})

    def patch(self,request,id):
        try:            
            stu = Student.objects.get(id=id)          
            serializer = StudentSerializer(stu , data=request.data ,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors)
       
        except Exception as e:
            return Response({"error": str(e)})
       
    def delete(self,request,id):
        try:            
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response("Delete Successfully")
        
        except Exception as e:
            return Response({"error": str(e)})   