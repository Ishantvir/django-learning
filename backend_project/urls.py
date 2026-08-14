from django.contrib import admin
from django.urls import path
from students.views import index, all_data, single_data, add_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('all/', all_data, name='all_data'),
    path('single/', single_data, name='single_data'),
    path('addstudent/', add_student, name='add_student')
]
