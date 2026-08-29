from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.db.models import Q
from students.models import Student
from students.forms import StudentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.serializers import *

# Create your views here.
def index(request):
    students = [
        {'id':101, 'name':'Ishant', 'course': 'Python', 'marks':91},
        {'id':102, 'name':'Rahul', 'course': 'Django', 'marks':86},
        {'id':103, 'name':'Aman', 'course': 'AI', 'marks':94}
    ]

    return render(request, 'student/index.html', context= {'page':'Student Management','student':students})

@login_required(login_url='/')
# @permission_required('students.view_student', raise_exception=True) #### import this with login_required, permission_requied like this need for future reference
def all_data(request):
    if not request.user.has_perm('students.view_student'):
        return HttpResponseForbidden('You Cannot View Document')
    all_students = Student.objects.all().order_by('id')
    return render(request, 'student/all.html', {'students': all_students})

@login_required(login_url='/')
def single_data(request ):
    search_term = request.GET.get('q', '')
    student = Student.objects.none()
    if search_term:
        student = Student.objects.filter(
        Q(name__icontains=search_term) |
        Q(city__icontains=search_term) |
        Q(email__icontains=search_term)
    )
    return render(request, 'student/single.html', {'student': student, 'search_term': search_term})

## old add (for my future reference)
# @login_required(login_url='/')
# def add_student(request):
#     if not request.user.has_perm('students.add_student'):
#             return HttpResponseForbidden('You Cannot Add Student.')
#     if request.method == 'POST':
#         addStu = StudentForm(request.POST)
#         if addStu.is_valid():
#             nm = addStu.cleaned_data['name']
#             em = addStu.cleaned_data['email']
#             ag = addStu.cleaned_data['age']
#             cu = addStu.cleaned_data['course']
#             ads = addStu.cleaned_data['address']
#             mks = addStu.cleaned_data['marks']
#             ct = addStu.cleaned_data['city']

#             ## Saved To Database
#             stu = Student(name = nm, email = em, age = ag, course = cu,address=ads, marks = mks, city = ct)
#             stu.save()
#             return HttpResponseRedirect('/addsuccess/')

#     else:
#         addStu = StudentForm(auto_id=True)
#         # addStu = StudentForm(initial={'email':'abc12@example.com'})
#         # addStu = StudentForm(label_suffix=':  ')
#         # addStu = StudentForm(auto_id=True, field_order=['name','city'])
#     return render(request, 'student/add_student.html', {'addStu':addStu})

## new add
@login_required(login_url='/')
def add_student(request):
    if not request.user.has_perm('students.add_student'):
            return HttpResponseForbidden('You Cannot Add Student.')
    if request.method == 'POST':
        addStu = StudentForm(request.POST)
        if addStu.is_valid():
            ## Saved To Database
            addStu.save()
            return HttpResponseRedirect('/addsuccess/')
    else:
        addStu = StudentForm(auto_id=True)
    return render(request, 'student/add_student.html', {'addStu':addStu})


@login_required(login_url='/')
def update_student(request, id):
    if not request.user.has_perm('students.change_student'):
        return HttpResponseForbidden('You Cannot Update Student.')
    
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        upStu = StudentForm(request.POST, instance=student)

        if upStu.is_valid():
            upStu.save()
            return HttpResponseRedirect('/updatesuccess/')

    else:
        upStu = StudentForm(instance=student)

    return render(request,'student/update_student.html',{'upStu': upStu})

@login_required(login_url='/')
def delete_student(request, id):
    if not request.user.has_perm('students.delete_student'):
        return HttpResponseForbidden('You Cannot Delete the Data.')
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('/')    
    return redirect('/')

def add_success(request):
    return render(request, 'student/success.html')

def update_success(request):
    return render(request, 'student/updatesuccess.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/')

        user =authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/')
        else:
            login(request, user)
            return redirect('/view/')

    return render(request, 'Auth/login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username Already Taken. Please Choose Another Username')
            return redirect('register_page')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, 'Registration Successful. Please Login to Continue')
        return redirect('register_page')

    return render(request, 'Auth/register.html')

def logout_page(request):
    logout(request)
    return redirect('/')


''' REST API '''
@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serailizer = StudentSerializer(student_objs.order_by('id'), many=True)
    return Response({'status': 200, 'payload': serailizer.data})

@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data = request.data)

    if not serializer.is_valid():
        return Response({'status': 403, 'error': serializer.errors, 'message':'Something went wrong.'})

    serializer.save()
    return Response({'status': 200, 'payload': serializer.data, 'message': 'Data Saved'})

@api_view(['PUT'])
def put_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)

        serializer = StudentSerializer(student_obj, data = request.data)
        
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors, 'message':'Something went wrong.'})
        
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'Data Saved'})

    except Exception as e:
        return Response({'status': 403, 'message':'Invalid id'})
    
@api_view(['PATCH'])
def patch_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)

        serializer = StudentSerializer(student_obj, data = request.data, partial=True)
        
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors, 'message':'Something went wrong.'})
        
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'Data Saved'})

    except Exception as e:
        return Response({'status': 403, 'message':str(e)})
    