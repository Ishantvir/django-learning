from django.contrib import admin
from students.models import Student

# Register your models here.
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id','name', 'email', 'course', 'city')

# admin.site.register(Student, StudentAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'course', 'city')
