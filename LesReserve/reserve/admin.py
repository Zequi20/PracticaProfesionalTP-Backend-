from django.contrib import admin
from .models import Cliente
from .models import Ciudad
from .models import Departamento
from .models import Habitacion
from .models import Hotel
from .models import Personal
from .models import Reserva


admin.site.register(Ciudad)
admin.site.register(Departamento)
admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(Hotel)
admin.site.register(Personal)
admin.site.register(Reserva)
# Register your models here.
