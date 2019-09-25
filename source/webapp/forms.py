from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Summary')
    description = forms.CharField(max_length=40, required=True, label='Description', widget=widgets.Textarea)
    status = forms.ChoiceField(choices=Status, required=True, label='Status')
    category = forms.ChoiceField(choices=Type, required=False, label='Type')