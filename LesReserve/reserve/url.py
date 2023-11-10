
from django.conf.urls import url
from LesReserve import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^departamento$',views.departamentoApi),
    url(r'^departamento/([0-9]+)$',views.departamentoApi),

    url(r'^personal$',views.personalApi),
    url(r'^personal/([0-9]+)$',views.personalApi),

    url(r'^ciudad$',views.ciudadApi),
    url(r'^ciudad/([0-9]+)$',views.ciudadApi),

    url(r'^cliente$',views.clienteApi),
    url(r'^cliente/([0-9]+)$',views.clienteApi),

    url(r'^hotel$',views.hotelApi),
    url(r'^hotel/([0-9]+)$',views.hotelApi),

    url(r'^habitacion$',views.habitacionApi),
    url(r'^habitacion/([0-9]+)$',views.habitacionApi),

    url(r'^servicio$',views.servicioApi),
    url(r'^servicio/([0-9]+)$',views.servicioApi),

    url(r'^reserva$',views.reservaApi),
    url(r'^reserva/([0-9]+)$',views.reservaApi),

    url(r'^resena$',views.resenaApi),
    url(r'^resena/([0-9]+)$',views.resenaApi),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)