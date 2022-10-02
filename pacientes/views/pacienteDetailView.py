from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from pacientes.models.paciente import Paciente
from pacientes.serializers.pacienteSerializer import PacienteSerializer


class PacienteDetailView(generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)