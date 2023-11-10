from django.test import TestCase
from django.urls import reverse

class InicioVistaTest(TestCase):
    def test_inicio_devuelve_200(self):
        url = reverse('vista_inicio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_inicio_no_vacia(self):
        url = reverse('vista_inicio')
        response = self.client.get(url)
        self.assertContains(response, '<ul', count=1)

class ClientesVistaTest(TestCase):

    def test_clientes_devuelve_200(self):
        url = reverse('vista_clientes') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_clientes_no_vacia(self):
        url = reverse('vista_clientes')
        response = self.client.get(url)
        self.assertContains(response, '<ul', count=1)

class ReservasVistaTest(TestCase):
    def test_reservas_devuelve_200(self):
        url = reverse('vista_reservas') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_reservas_no_vacia(self):
        url = reverse('vista_reservas')
        response = self.client.get(url)
        self.assertContains(response, '<ul', count=1)