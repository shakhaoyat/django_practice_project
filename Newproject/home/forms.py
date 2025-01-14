from django import forms
from home.models import student

class studentForm(forms.ModelForm):
      class Meta:
            model = student
            fields = '__all__'
class infoForm(form.Form):
      name = form.forms.CharField(max_length=100)