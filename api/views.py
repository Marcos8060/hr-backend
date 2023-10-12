from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics,status,permissions
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# CUSTOMIZING TOKENS
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# Create your views here.
class RegistrationView(APIView):
    permission_classes = [permissions.AllowAny]  # Ensure only admin users can access this view

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class PermissionsView(generics.ListAPIView):
    serializer_class = PermissionSerializer

    def get_queryset(self):
        user_id = self.kwargs['userId']
        user = get_object_or_404(Employee, id=user_id)
        
        # Check if the user has a role assigned
        if user.role:
            permissions = Permission.objects.filter(role=user.role)
            return permissions
        else:
            # If the user does not have a role assigned, return an empty queryset
            return Permission.objects.none()

    

class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = AllPermissionsSerializer


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class AllUsersView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = UsersSerializer
   

class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    


class ProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LeaveDetailsView(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

