from django.urls import path
from reserve import views

urlpatterns = [
    path('departamento/', views.departamento_api, name='departamento'),
    path('departamento/<int:id>/', views.departamento_api, name='departamento_api_detail'),
    path('departamento/savefile/', views.save_file, name='save_file'),
]