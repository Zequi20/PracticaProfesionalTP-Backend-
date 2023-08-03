# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length= 50)
    id_departamento = models.ForeignKey('Departamento', on_delete=models.PROTECT, db_column='id_departamento', blank=True, null=True)

    """ class Meta:
        managed = False
        db_table = 'Ciudad' """
# Unable to inspect table 'Cliente'
# The error was: list index out of range

class Cliente(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length= 50)
    apellido = models.CharField(blank=True, null=True, max_length= 50)
    id_ciudad = models.ForeignKey('Ciudad', db_column='id_ciudad', on_delete=models.PROTECT, blank=True, null=True)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    ci = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    




class Departamento(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length= 50)

  

class Habitacion(models.Model):
    id_hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, db_column='id_hotel', blank=True, null=True)
    tipo = models.CharField(blank=True, null=True, max_length= 50)  # This field type is a guess.
    numero = models.SmallIntegerField(blank=True, null=True)
    precio = models.PositiveBigIntegerField() # This field type is a guess.
    descripcion = models.CharField(blank=True, null=True, max_length= 50)
    capacidad = models.PositiveIntegerField()  # This field type is a guess.
    estado = models.CharField(blank=True, null=True, max_length=20)



class Hotel(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length=50)
    direccion = models.CharField(blank=True, null=True, max_length=50)
    telefono = models.CharField(blank=True, null=True, max_length=50)
    correo = models.CharField(blank=True, null=True, max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, db_column='id_ciudad', blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=20)

   


class Personal(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length=50)
    fecha_alta = models.DateField(blank=True, null=True)
    apellido = models.CharField(blank=True, null=True, max_length=50)
    ci = models.CharField(blank=True, null=True, max_length=20)
    telefono = models.CharField(blank=True, null=True, max_length=50)
    correo = models.CharField(blank=True, null=True, max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, db_column='id_ciudad', blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=50)


class Reserva(models.Model):
    
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='id_cliente', blank=True, null=True)
    id_habitacion = models.ForeignKey(Habitacion, on_delete=models.PROTECT, db_column='id_habitacion', blank=True, null=True)
    id_personal = models.ForeignKey(Personal, on_delete=models.PROTECT, db_column='id_personal', blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=50)
    observacion = models.CharField(blank=True, null=True, max_length=500)



