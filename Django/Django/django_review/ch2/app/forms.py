from django import forms 

class Registration(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField(max_length=50)