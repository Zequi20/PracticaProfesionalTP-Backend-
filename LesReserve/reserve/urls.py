from django.urls import path
from .views import ClienteView, CiudadView, DepartamentoView, HabitacionView, HotelView, PersonalView

urlpatterns = [
    path('clientes', ClienteView.as_view(), name='api-clientes'),
    path('ciudades', CiudadView.as_view(), name='api-ciudades'),
    path('departamentos', DepartamentoView.as_view(), name='api-departamentos'),
    path('habitaciones', HabitacionView.as_view(), name='api-habitaciones'),
    path('hoteles', HotelView.as_view(), name='api-hoteles'),
    path('personal', PersonalView.as_view(), name='api-personal'),
]
