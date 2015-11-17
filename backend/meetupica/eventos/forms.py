from django import forms

from .models import LugarEvento, Evento, Taller


class LugarEventoForm(forms.ModelForm):

    class Meta:
        model = LugarEvento
        fields = ('nombre', 'ubicacion', 'latitud', 'altitud', 'calificacion')


class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('nombre', 'fecha', 'descripcion', 'lugar_evento')


class TallerForm(forms.ModelForm):

    class Meta:
        model = Taller
        fields = ('nombre', 'descripcion', 'horario', 'ponente', 'evento')
