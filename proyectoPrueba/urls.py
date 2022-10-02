from pacientes import views
from django.db import router
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
   # path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('registrarPaciente/', views.PacienteCreateView.as_view()),
    path('obtenerInfoPaciente/<int:pk>', views.PacienteGetView.as_view()),
    path('infoPersonal/', views.PacienteDetailView.as_view()),
    path('editarPaciente/<int:pk>/', views.PacienteUpdateView.as_view()),
    path('eliminarPaciente/<int:pk>/', views.PacienteDeleteView.as_view()),
 
]