from django.db import models

class Departamento(models.Model):
    departamentoId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'departamento'
    



class Ciudad(models.Model):
    ciudadId = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    id_departamento = models.ForeignKey('Departamento', on_delete=models.PROTECT, db_column='id_departamento', blank=True, null=True)

    def __str__(self):
        if self.id_departamento:
            return f"{self.nombre} - {self.id_departamento.nombre}"
        else:
            return self.nombre

    class Meta:
        managed = False
        db_table = 'Ciudad'

class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    ci = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    foto = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cliente'






class Hotel(models.Model):
    hotelId = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    direccion = models.CharField(blank=True, null=True, max_length=50)
    telefono = models.CharField(blank=True, null=True, max_length=50)
    correo = models.CharField(blank=True, null=True, max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, db_column='ciudadId', blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'Hotel'

class Habitacion(models.Model):
    habitacionId = models.AutoField(primary_key=True)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, db_column='id_hotel', blank=True, null=True)
    tipo = models.CharField(blank=True, null=True, max_length=50)
    numero = models.SmallIntegerField(blank=True, null=True)
    precio = models.PositiveBigIntegerField()
    descripcion = models.CharField(blank=True, null=True, max_length=500)
    foto = models.CharField(blank=True, null=True, max_length=500)
    capacidad = models.PositiveIntegerField()
    estado = models.CharField(blank=True, null=True, max_length=20)
    class Meta:
        managed = False
        db_table = 'Habitacion'

class Personal(models.Model):
    personalId = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    apellido = models.CharField(blank=True, null=True, max_length=50)
    fecha_alta = models.DateField(blank=True, null=True)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, db_column='id_hotel', blank=True, null=True)
    puesto = models.CharField(blank=True, null=True, max_length=50)
    ci = models.CharField(blank=True, null=True, max_length=20)
    telefono = models.CharField(blank=True, null=True, max_length=50)
    correo = models.CharField(blank=True, null=True, max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, db_column='ciudadId', blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=50)
    foto = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'Personal'

class Servicio(models.Model):
    servicioId = models.AutoField(primary_key=True)
    precio = models.PositiveBigIntegerField()
    servicio_tipo = models.CharField(blank=True, null=True, max_length=500)
    detalle = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'Servicio'

class Reserva(models.Model):
    reservaId = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT, db_column='id_cliente', blank=True, null=True)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, db_column='id_servicio', blank=True, null=True)
    id_habitacion = models.ForeignKey('Habitacion', on_delete=models.PROTECT, db_column='id_habitacion', blank=True, null=True)
    id_personal = models.ForeignKey('Personal', on_delete=models.PROTECT, db_column='id_personal', blank=True, null=True)
    cantidad = models.SmallIntegerField(default=0)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=50)
    observacion = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'Reserva'

class Resena(models.Model):
    resenaId = models.AutoField(primary_key=True)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=True, null=True)
    comentario = models.CharField(max_length=500, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Resena'