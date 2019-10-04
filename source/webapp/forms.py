from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Summary')
    description = forms.CharField(max_length=3000, required=True, label='Description', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects, required=True, label='Status', empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects, required=False, label='Type', empty_label=None)

class StatusForm(forms.Form):
    new_status = forms.CharField(max_length=50, required=True, label='New_status')


class TypeForm(forms.Form):
    new_type = forms.CharField(max_length=50, required=True, label='New_type')