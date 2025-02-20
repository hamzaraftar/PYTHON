from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view(["GET"])
# def hello_world(request):
#     return Response({"message":"Hello world"})

@api_view(["POST"])
def hello_world(request):
    if request.method == "POST":
        print(request.data.get("name"))
        print(request.data.get("rollNo"))
        print(request.data.get("age"))
        return Response({"message":"Hello post request"})