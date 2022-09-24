from dataclasses import fields
from pyexpat import model
from django.forms import forms

from .models import Doctor

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = "__all__"

