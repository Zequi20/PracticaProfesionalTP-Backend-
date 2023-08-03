from django.contrib import admin
from .models import Cliente
from .models import Ciudad
from .models import Departamento
from .models import Habitacion
from .models import Hotel
from .models import Personal
from .models import Reserva


class CiudadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'id_departamento']
    list_filter = ['nombre']
    ordering = ['-nombre']


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    ordering = ['-nombre']


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    ordering = ['-nombre']


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['ci',
                    'nombre',
                    'apellido',
                    'telefono',
                    'correo'
                    ]
    list_filter = ['ci',
                   'nombre',
                   'apellido',
                   'telefono',
                   'correo']

    ordering = ['-ci',
                '-nombre']
    search_fields=('ci','nombre','apellido')


class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['id_hotel',
                    'numero',
                    'precio',
                    'descripcion',
                    'capacidad'

                    ]
    list_filter = ['id_hotel',
                    'numero',
                    'precio',
                    'descripcion',
                    'capacidad']

    ordering = ['id_hotel',
                    'numero',
                    'precio',
                    'capacidad']
    search_fields=('numero','capacidad')

class HotelAdmin(admin.ModelAdmin):
    list_display = ['nombre',
                    'direccion',
                    'id_ciudad',
                    'estado',
                    ]
    list_filter = ['nombre',
                    'direccion',
                    'id_ciudad',
                    'estado',]

    ordering = ['nombre',
                    'direccion',
                    'id_ciudad',
                    'estado',]
    search_fields=('nombre',)

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['nombre',
                    'apellido',
                    'id_hotel',
                    'puesto',
                    'telefono',
                    ]
    list_filter = ['nombre',
                    'apellido',
                    'id_hotel',
                    'puesto',
                    'telefono',
                    ]

    ordering = ['nombre',
                    'apellido',
                    'id_hotel',
                    'puesto',
                    'telefono',
                    ]
    search_fields=('ci','nombre','apellido')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id_habitacion',
                    'id_personal',
                    'cantidad',
                    'fecha_inicio',
                    'fecha_fin',
                    'observacion'
                    ]
    list_filter = ['id_habitacion',
                    'id_personal',
                    'cantidad',
                    'fecha_inicio',
                    'fecha_fin',
                    'observacion'
                    ]

    ordering = ['id_habitacion',
                    'id_personal',
                    'cantidad',
                    'fecha_inicio',
                    'fecha_fin',
                    'observacion'
                    ]
    search_fields=('fecha_inicio',)

admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Reserva, ReservaAdmin)
# Register your models here.
