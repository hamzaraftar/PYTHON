from django import forms
from .models import Profile

class Registration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','password']
