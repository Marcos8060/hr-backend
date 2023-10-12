from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('create_account',RegistrationView.as_view()),
    path('project', ProjectView.as_view()),
    path('roles',RoleListView.as_view()),
    path('users',AllUsersView.as_view()),
    path('project/<int:pk>/', ProjectDetailsView.as_view()),
    path('permissions/<int:userId>',PermissionsView.as_view()),
    path('all-permissions',PermissionListView.as_view()),


     # TOKEN
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
