from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()