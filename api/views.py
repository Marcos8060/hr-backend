from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        reg_serializer = UserSerializer(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        reg_serializer.save()
        return Response(reg_serializer.data)
