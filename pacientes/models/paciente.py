# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

TIPOS_CHOICES = [('CC','CC'),('TI','TI'),('RC','RC')]

class Paciente(models.Model):
    paciente_documento = models.BigIntegerField(primary_key=True)
    paciente_tipodocumento = models.CharField(choices= TIPOS_CHOICES,max_length=2)
    paciente_primernombre = models.CharField(max_length=60)
    paciente_segundonombre = models.CharField(max_length=60, blank=True, null=True)
    paciente_primerapellido = models.CharField(max_length=60)
    paciente_segundoapellido = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'
        unique_together = (('paciente_documento', 'paciente_tipodocumento'),)
