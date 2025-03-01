from django import forms

class Registeration(forms.Form):
    frist_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()