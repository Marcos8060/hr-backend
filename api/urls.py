from django.urls import path
from .views import RegisterView,LoginView,ProjectView,ProjectDetailsView


urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('project',ProjectView.as_view()),
    path('project/<int:pk>/',ProjectDetailsView.as_view()),
]