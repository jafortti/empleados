from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import (
    ListAllEmpleados,
    ListByAreaEmpleado,
    ListEmpleadoByKword,
    ListByTrabajoEmpleado,
    ListHabilidadesEmpleados,
    EmpleadoDetailView,
    EmpleadoCreateView,
    SuccessView,
    EmpleadoUpdateView,
    EmpleadoDeleteView,
    InicioView,
    ListEmpleadosAdmin

)

app_name='persona_app' #estandar de nombre usado por la comunidad
urlpatterns = [
    path('',InicioView.as_view(),name='inicio'),
    path(
        'listar-todo-empleados/',
        ListAllEmpleados.as_view(),
        name="empleados_all"
        ),
    path(
        'listar-by-area/<shorname>/',
         ListByAreaEmpleado.as_view(),
          name='empleados_area'
          ),
    path(
        'lista-empleados-admin/',
         ListEmpleadosAdmin.as_view(),
          name='lista_empleados'
          ),
    path('buscar-empleado/',ListEmpleadoByKword.as_view()),
    path('listar-by-job/', ListByTrabajoEmpleado.as_view()),
    path('listar-habilidades/', ListHabilidadesEmpleados.as_view()),
    path('detail-empleado/<pk>/', EmpleadoDetailView.as_view(), name="detail_empleado"),
    path(
        'add-empleado/',
         EmpleadoCreateView.as_view(),
         name="empleado_add"
         ),
    path('success/', SuccessView.as_view(),name='correcto'),
    path('update-empleado/<pk>',EmpleadoUpdateView.as_view(),name='modificar'),
    path('eliminar-empleado/<pk>',EmpleadoDeleteView.as_view(),name='eliminar')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)