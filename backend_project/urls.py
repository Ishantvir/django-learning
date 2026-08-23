from django.contrib import admin
from django.urls import path
from students.views import index, all_data, single_data, add_student, add_success, update_student, update_success, delete_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_data, name='all_data'),
    path('all/', index, name='index'),
    path('single/', single_data, name='single_data'),
    path('addstudent/', add_student, name='add_student'),
    path('updatestudent/<int:id>/', update_student, name='update_student'),
    path('deletestudent/<int:id>/', delete_student, name='delete_student'),
    path('addsuccess/', add_success, name='add_success'),
    path('updatesuccess/', update_success, name='update_success')
]
