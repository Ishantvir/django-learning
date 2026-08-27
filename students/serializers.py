from rest_framework import serializers
from students.models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        ''' Use any one from below'''
        # fields = ['name', 'email','age','course']
        exclude = ['id', 'user']
        # fields = '__all__'