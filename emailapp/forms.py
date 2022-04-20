from dataclasses import fields
from django import forms
from emailapp.models import stud

class studentmail(forms.ModelForm):
    class Meta:
        model = stud
        fields = '__all__'