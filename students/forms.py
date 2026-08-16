from django import forms
from students.models import Student

# class StudentForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     age =  forms.IntegerField()
#     course = forms.CharField()
#     address = forms.Textarea()
#     marks = forms.IntegerField()
#     city = forms.CharField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','age', 'course', 'address','marks', 'city']
        labels = {'name':'Enter Name', 'email': 'Enter Email'}
        error_messages = {
            'email':{'requires':'Email is required.'}
        }