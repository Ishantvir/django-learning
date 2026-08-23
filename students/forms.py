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

    def clean_marks(self):
        marks = self.cleaned_data['marks']
        if marks < 0 or marks > 100:
            raise forms.ValidationError('Marks must be between 0 to 100.')
        return marks

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0:
            raise forms.ValidationError('Age must be greater than 0.')
        return age

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('Name should not contain numbers.')
        return name

    def clean(self):
        cleaned_data = super().clean()

        marks = cleaned_data.get('marks')
        course = cleaned_data.get('course')

        if marks is not None and course:
            if marks < 40 and course == "Advanced Django":
                raise forms.ValidationError('Student with marks below 40 connot join Advanced Django.')
            return cleaned_data