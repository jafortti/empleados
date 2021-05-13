from django.urls import path
from .views import NewDepartamentoView,DepartamentoListView

def DesdeApp(self):
    print('====================Desde aplicación Departamento==================================')

app_name='departamento_app'
urlpatterns = [
    path(
        'departamento-lista/',
        DepartamentoListView.as_view(),
        name='departamento_list'
        ),
    path('new-departamento/',NewDepartamentoView.as_view(),name='nuevo_departamento'),
]