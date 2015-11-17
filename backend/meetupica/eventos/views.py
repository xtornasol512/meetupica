from django.shortcuts import render
from django.views.generic import ListView, View, CreateView, UpdateView, DeleteView, TemplateView

from braces.views import LoginRequiredMixin

from .models import LugarEvento, Evento, Taller
# Create your views here.

class LugarEventoCreateView(LoginRequiredMixin, CreateView):
    model = LugarEvento
    form_class = LugarEventoForm
    template_name = 'lugar_evento/lugar_evento_create.html'


class LugarEventoUpdateView(LoginRequiredMixin, UpdateView):
    model = LugarEvento
    form_class = LugarEventoForm
    template_name = 'lugar_evento/lugar_evento_update.html'


class LugarEventoListView(LoginRequiredMixin, ListView):
    model = LugarEvento
    form_class = LugarEventoForm
    template_name = 'lugar_evento/lugar_evento_list.html'


class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento/evento_create.html'


class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = LugarEvento
    form_class = LugarEventoForm
    template_name = 'evento/evento_update.html'


class EventoListView(LoginRequiredMixin, ListView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento/evento_list.html'


class TallerCreateView(LoginRequiredMixin, CreateView):
    model = Taller
    form_class = TallerForm
    template_name = 'taller/taller_create.html'


class TallerUpdateView(LoginRequiredMixin, UpdateView):
    model = LugarEvento
    form_class = TallerForm
    template_name = 'taller/taller_update.html'


class TallerListView(LoginRequiredMixin, ListView):
    model = LugarEvento
    form_class = TallerForm
    template_name = 'taller/taller_list.html'


