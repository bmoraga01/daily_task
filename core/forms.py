from django.forms import ModelForm, Form, TextInput, Select, DateInput, FileInput
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'other_gender', 'birth_date', 'location', 'phone_number', 'profile_image']
        
        widgets = {
            'gender': Select(attrs={ 'class': 'form-control' }),
            'other_gender': TextInput(attrs={ 'class': 'form-control' }),
            'location': TextInput(attrs={ 'class': 'form-control' }),
            'phone_number': TextInput(attrs={ 'class': 'form-control' }),
            'profile_image': FileInput(attrs={ 'class': 'form-control', 'accept': 'image/png, image/jpg, image/jpeg' }),
        }