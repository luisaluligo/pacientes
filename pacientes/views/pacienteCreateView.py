from rest_framework import status, views
from rest_framework.response import Response

from pacientes.serializers.pacienteSerializer import PacienteSerializer


class PacienteCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)