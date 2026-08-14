from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    age =  forms.IntegerField()
    course = forms.CharField()
    address = forms.Textarea()
    marks = forms.IntegerField()
    city = forms.CharField()