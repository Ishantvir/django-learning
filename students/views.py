from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def index(request):
    students = [
        {'id':101, 'name':'Ishant', 'course': 'Python', 'marks':91},
        {'id':102, 'name':'Rahul', 'course': 'Django', 'marks':86},
        {'id':103, 'name':'Aman', 'course': 'AI', 'marks':94}
    ]

    return render(request, 'student/index.html', context= {'page':'Student Management','student':students})