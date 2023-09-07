from rest_framework.views import APIView
from .serializers import UserSerializer,ProjectSerializer
from rest_framework.response import Response
from rest_framework import generics,status
from .models import User,Project
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated


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

class RegisterView(APIView):
    def post(self, request):
        reg_serializer = UserSerializer(data=request.data)
        if reg_serializer.is_valid():
            email = reg_serializer.validated_data.get('email')
            if User.objects.filter(email=email).exists():
               error_message = "Email already exists"
               return Response(
                 {"success": False, "message": error_message},
                    status=status.HTTP_400_BAD_REQUEST
                  )
            else:
                reg_serializer.save()
                return Response(
                    {"success": True, "message": "Registration successful"},
                    status=status.HTTP_201_CREATED
                )
        else:
            error_message = reg_serializer.errors.get('email', '')
            return Response(
                {"success": False, "message": error_message},
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(MyTokenObtainPairView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User does not exist')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        


class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    



class ProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

