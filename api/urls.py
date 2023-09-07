from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('project', ProjectView.as_view()),
    path('project/<int:pk>/', ProjectDetailsView.as_view()),
    path('permissions/<int:userId>',PermissionsView.as_view()),


     # TOKEN
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
