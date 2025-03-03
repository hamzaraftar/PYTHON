from django import forms

class StudentRegistratoion(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()