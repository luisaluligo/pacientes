# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .paciente import Paciente
from .patologia import Patologia

class Pacientepatologias(models.Model):
    pacpat_codigo = models.BigIntegerField(primary_key=True)
    patologia_codigo = models.ForeignKey(Patologia, models.DO_NOTHING, db_column='patologia_codigo')
    paciente_documento = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_documento')

    class Meta:
        managed = False
        db_table = 'pacientepatologias'

