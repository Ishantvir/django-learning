from django.contrib import admin
from django.urls import path
from students.views import index, all_data, single_data, add_student, add_success, update_student, update_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('all/', all_data, name='all_data'),
    path('single/<int:id>/', single_data, name='single_data'),
    path('addstudent/', add_student, name='add_student'),
    path('updatestudent/<int:id>/', update_student, name='update_student'),
    path('addsuccess/', add_success, name='add_success'),
    path('updatesuccess/', update_success, name='update_success')
]
