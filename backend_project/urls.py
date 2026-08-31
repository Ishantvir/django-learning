from django.contrib import admin
from django.urls import path
from students.views import index, all_data, single_data, add_student, add_success, update_student, update_success, delete_student, login_page, register_page, logout_page, home, post_student, put_student, patch_student, del_student

urlpatterns = [
    path('', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_page, name='logout_page'),
    path('admin/', admin.site.urls),
    path('view/', all_data, name='all_data'),
    path('all/', index, name='index'),
    path('single/', single_data, name='single_data'),
    path('addstudent/', add_student, name='add_student'),
    path('updatestudent/<int:id>/', update_student, name='update_student'),
    path('deletestudent/<int:id>/', delete_student, name='delete_student'),
    path('addsuccess/', add_success, name='add_success'),
    path('updatesuccess/', update_success, name='update_success'),
    path('home/', home , name='home'),
    path('poststu/', post_student , name='post_student'),
    path('updatestu/<int:id>/', put_student , name='put_student'),
    path('patchstu/<int:id>/', patch_student , name='patch_student'),
    path('delstu/<int:id>/', del_student , name='del_student')
]
