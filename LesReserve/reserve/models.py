# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'asigancion'
# The error was: list index out of range


class Clientes(models.Model):
    nombre = models.CharField(blank=True, null=True)
    correo = models.CharField(blank=True, null=True)
    telefono = models.CharField(blank=True, null=True)
    direccion = models.CharField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Habitaciones(models.Model):
    id_hotel = models.ForeignKey('Hoteles', models.DO_NOTHING, db_column='id_hotel', blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)  # This field type is a guess.
    medidas = models.CharField(blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.
    descripcion = models.CharField(blank=True, null=True)
    capacidad = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'habitaciones'


class Hoteles(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    nombre = models.CharField(blank=True, null=True)
    direccion = models.CharField(blank=True, null=True)
    telefono = models.CharField(blank=True, null=True)
    habitaciones = models.SmallIntegerField(blank=True, null=True)
    pisos = models.TextField(blank=True, null=True)  # This field type is a guess.
    correo = models.CharField(blank=True, null=True)
    ciudad = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hoteles'
# Unable to inspect table 'personal'
# The error was: list index out of range


class Puestos(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puestos'


class Reservas(models.Model):
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_habitacion = models.ForeignKey(Habitaciones, models.DO_NOTHING, db_column='id_habitacion', blank=True, null=True)
    fecha_entrada = models.DateField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'reservas'
