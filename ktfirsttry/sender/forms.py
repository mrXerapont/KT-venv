from datetime import datetime

from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput
from django.contrib.admin import widgets





from .models import Snd, Repeat_type



class SndForm(ModelForm):
    class Meta:
        model = Snd
        description = forms.CharField()
        mailto = forms.EmailField()
        text = forms.CharField()
        fields = ('description', 'mailto', 'text', 'dtime', 'repeat')
 #   dtime = forms.DateTimeField(widget=DateTimeWidget())

    dtime = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime, label='Дата и время отправки')



