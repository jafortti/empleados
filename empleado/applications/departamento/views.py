from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from.forms import NewDepartamentoForm
from.models import Departamento
# Modelos
from applications.persona.models import Persona



class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name='departamentos'

class NewDepartamentoView(FormView):
    template_name='departamento/new_departamento.html'
    form_class=NewDepartamentoForm
    success_url='/'

    def form_valid(self,form):
        depa=Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=['shorname']
        )
        depa.save()
        nombre=form.cleaned_data['nombre']
        apellido=form.cleaned_data['apellidos']
        Persona.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa

        )
        return super(NewDepartamentoView,self).form_valid(form)

