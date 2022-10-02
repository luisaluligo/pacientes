from rest_framework import serializers
from pacientes.models.paciente import Paciente
from pacientes.models.pacientePatologias import Pacientepatologias
from pacientes.serializers.pacientepatologiasSerializer import PacientepatologiaSerializer

class PacienteSerializer(serializers.ModelSerializer):
    patologias = PacientepatologiaSerializer()

    class Meta:
        model = Paciente
        fields = ['paciente_documento','paciente_tipodocumento', 'paciente_primernombre',  'paciente_segundonombre', 'paciente_primerapellido', 'paciente_segundoapellido', 'patologias']
       

    def create(self, validated_data):
        patologiaData = validated_data.pop('patologias')
        pacienteInstance = Paciente.objects.create(**validated_data)
        Pacientepatologias.objects.create(paciente_documento=pacienteInstance, **patologiaData)
        return pacienteInstance
        
    def update(self, instance, validated_data):
        patologiaData = validated_data.pop('patologias')
        instance.paciente_primernombre = validated_data.get("paciente_primernombre", instance.paciente_primernombre)
        instance.paciente_segundonombre = validated_data.get("paciente_segundonombre", instance.paciente_segundonombre)
        instance.paciente_primerapellido = validated_data.get("paciente_primerapellido", instance.paciente_primerapellido)
        instance.paciente_segundoapellido = validated_data.get("paciente_segundoapellido", instance.paciente_segundoapellido)
        instance.save()
        patologia =Pacientepatologias.objects.get(paciente_documento=instance.paciente_documento)
        patologia.patologia_codigo = patologiaData.get("patologia_codigo", patologia.patologia_codigo)
        patologia.save()

    def to_representation(self, obj):
        paciente = Paciente.objects.get(paciente_documento=obj.paciente_documento)
        patologia = Pacientepatologias.objects.get(paciente_documento=obj.paciente_documento)
        return{
            'documento': paciente.paciente_documento,
            'primerNombre': paciente.paciente_primernombre,
            'segundoNombre': paciente.paciente_segundonombre,
            'primerApellido': paciente.paciente_primerapellido,
            'segundoApellido': paciente.paciente_segundoapellido,
            'patologias':{ 'patologia_codigo' : patologia.codigo_tipnov,
                             'patologia_nombre' : patologia.nombre_tipnov
                               },
            
        }
        
         