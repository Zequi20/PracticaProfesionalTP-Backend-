# Generated by Django 4.1.5 on 2023-08-03 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_delete_nuevomodelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='puesto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('observacion', models.CharField(blank=True, max_length=500, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.cliente')),
                ('id_habitacion', models.ForeignKey(blank=True, db_column='id_habitacion', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.habitacion')),
                ('id_personal', models.ForeignKey(blank=True, db_column='id_personal', null=True, on_delete=django.db.models.deletion.PROTECT, to='reserve.personal')),
            ],
        ),
    ]
