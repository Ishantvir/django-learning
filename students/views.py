from django.shortcuts import render 
from students.models import Student

# Create your views here.
def index(request):
    students = [
        {'id':101, 'name':'Ishant', 'course': 'Python', 'marks':91},
        {'id':102, 'name':'Rahul', 'course': 'Django', 'marks':86},
        {'id':103, 'name':'Aman', 'course': 'AI', 'marks':94}
    ]

    return render(request, 'student/index.html', context= {'page':'Student Management','student':students})

def all_data(request):
    all_students = Student.objects.all()
    return render(request, 'student/all.html', {'students': all_students})

def single_data(request):
    student= Student.objects.get(id=1)
    return render(request, 'student/single.html', {'student': student})
