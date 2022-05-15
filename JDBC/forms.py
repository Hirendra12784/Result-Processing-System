from django import forms
from JDBC.models import Student



class Sforms(forms.ModelForm):
  class Meta:
    model=Student
    fields="__all__"

