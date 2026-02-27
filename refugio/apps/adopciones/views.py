from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.adopciones.models import Solicitud, Persona
from apps.adopciones.forms import SolicitudForm, PersonaForm, SolicitudEstadoForm


def index(request):
    return HttpResponseRedirect(reverse_lazy('adopciones:solicitud_listar'))


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopciones/solicitud_list.html'


class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopciones/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopciones:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(UpdateView):
    model = Solicitud
    template_name = 'adopciones/solicitud_update.html'
    form_class = SolicitudEstadoForm
    success_url = reverse_lazy('adopciones:solicitud_listar')


class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopciones/solicitud_delete.html'
    success_url = reverse_lazy('adopciones:solicitud_listar')
