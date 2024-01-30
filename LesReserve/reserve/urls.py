from django.urls import path

from reserve import views

urlpatterns = [
    path('departmento/', views.departamentoApi, name='departamento'),
    path('departmento/<int:id>/', views.departamentoApi, name='departamento_api_detail'),

    path('departamento/savefile/', views.SaveFile, name='save_file'),
]