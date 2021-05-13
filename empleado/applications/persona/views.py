from django.shortcuts import render
from django.urls import reverse_lazy

# models
from.models import Persona
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

#forms
from .forms import EmpleadoForm
# Create your views here.

class InicioView(TemplateView):
    ''' Vista que carga la pagina de inicio'''
    template_name='inicio.html'
# Create your views here.
def listar_empleados(Persona):
    listado=Persona.objects.all()
    return listado

class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by=4
    ordering=['first_name',]
    context_object_name='empleados'
    #queryset=listar_empleados(Persona)
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        queryset = Persona.objects.filter(
            full_name__icontains=palabra_clave
            )
        return queryset

class ListByAreaEmpleado(ListView):
    ''' Lista empleado de un area'''
    template_name="persona/list_by_area.html"
    context_object_name='listado'

    def get_queryset(self):
        area=self.kwargs['shorname']
        queryset = Persona.objects.filter(departamento__shor_name=area)
        return queryset
    
class ListEmpleadoByKword(ListView):
    ''' Lista empleado de un area desde formulario'''
    template_name="persona/by_kword.html"
    context_object_name='empleado'

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        queryset = Persona.objects.filter(departamento__name=palabra_clave)
        return queryset

class ListByTrabajoEmpleado(ListView):
    ''' Lista empleado por trabajo'''
    template_name="persona/list_by_job.html"
    context_object_name='listado'

    def get_queryset(self):
        queryset = Persona.objects.filter(job='0')
        return queryset
    

class ListHabilidadesEmpleados(ListView):
    template_name="persona/habilidades.html"
    context_object_name='habilidades'

    def get_queryset(self):
        empleado = Persona.objects.get(id=4)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "persona/detail_empleado.html"

class SuccessView(TemplateView):
    template_name="persona/success.html"

class EmpleadoCreateView(CreateView):
    model = Persona
    template_name = "persona/add.html"
    form_class=EmpleadoForm
    success_url=reverse_lazy('persona_app:lista_empleados')

    def form_valid(self,form):
        persona=form.save(commit=False)
        persona.full_name=persona.first_name + ' ' + persona.last_name
        persona.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Persona
    template_name = "persona/update-empleado.html"
    fields=[
    'first_name',
    'last_name',
    'job',
    'departamento',
    'habilidades',
    ]
    success_url=reverse_lazy('persona_app:lista_empleados')

    def form_valid(self,form):
        persona=form.save(commit=False)
        persona.save()
        return super(EmpleadoUpdateView,self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = "persona/delete.html"
    success_url=reverse_lazy('persona_app:lista_empleados')


class ListEmpleadosAdmin(ListView):
    template_name = "persona/lista_empleados.html"
    paginate_by=10
    ordering=['first_name',]
    context_object_name='empleados'
    model=Persona
    #queryset=listar_empleados(Persona)
   