from django.shortcuts import render
from django.http import HttpResponseRedirect
from students.models import Student
from students.forms import StudentForm

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

def single_data(request, id):
    student= Student.objects.get(id=id)
    return render(request, 'student/single.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        addStu = StudentForm(request.POST)
        if addStu.is_valid():
            nm = addStu.cleaned_data['name']
            em = addStu.cleaned_data['email']
            ag = addStu.cleaned_data['age']
            cu = addStu.cleaned_data['course']
            mks = addStu.cleaned_data['marks']
            ct = addStu.cleaned_data['city']

            ## Saved To Database
            stu = Student(name = nm, email = em, age = ag, course = cu, marks = mks, city = ct)
            stu.save()
            return HttpResponseRedirect('/addsuccess/')

    else:
        addStu = StudentForm(auto_id=True)
        # addStu = StudentForm(initial={'email':'abc12@example.com'})
        # addStu = StudentForm(label_suffix=':  ')
        # addStu = StudentForm(auto_id=True, field_order=['name','city'])
    return render(request, 'student/add_student.html', {'addStu':addStu})

def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        upStu = StudentForm(request.POST, instance=student)

        if upStu.is_valid():
            upStu.save()
            return HttpResponseRedirect('/updatesuccess/')

    else:
        upStu = StudentForm(instance=student)

    return render(request,'student/update_student.html',{'upStu': upStu})

def add_success(request):
    return render(request, 'student/success.html')

def update_success(request):
    return render(request, 'student/updatesuccess.html')