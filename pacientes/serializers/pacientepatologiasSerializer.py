from rest_framework import serializers
from pacientes.models.pacientePatologias import Pacientepatologias

class PacientepatologiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pacientepatologias
        fields = ['pacpat_codigo','patologia_codigo']
       

    def create(self, validated_data):
        pacientePatologiaInstance = pacientePatologiaInstance.objects.create(**validated_data)
        
        return pacientePatologiaInstance
