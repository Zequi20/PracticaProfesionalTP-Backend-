# Generated by Django 5.0 on 2024-02-20 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0005_personal_id_hotel_reserva_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicioId', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.PositiveBigIntegerField()),
                ('servicio_tipo', models.CharField(blank=True, max_length=500, null=True)),
                ('detalle', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='habitacion',
            name='foto',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('resenaId', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.cliente')),
                ('id_hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.hotel')),
            ],
        ),
    ]