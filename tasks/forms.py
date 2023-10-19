from django import forms
from .models import *

class DailyTaskForm(forms.ModelForm):
    class Meta:
        model = DailyTask
        fields = ['name', 'description', 'limit_date']
        
        widgets = {
            'name': forms.TextInput(attrs={ 'class': 'form-control', 'required': True }),
            'description': forms.Textarea(attrs={ 'class': 'form-control' }),
        }