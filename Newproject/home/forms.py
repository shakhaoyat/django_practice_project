from django import forms
from home.models import student

class studentForm(forms.ModelForm):
      class Meta:
            model = student
            fields = '__all__'