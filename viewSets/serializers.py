from rest_framework import serializers
from students.models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        ''' Use any one from below'''
        # fields = ['name', 'email','age','course']
        exclude = ['id', 'user']
        # fields = '__all__'

    def validate(self, data):
        if data.get('name'):
            for n in data.get('name'):
                if n.isdigit():
                    raise serializers.ValidationError({'error':'Name Should not contain numbers.'})

        if 'age' in data and (data.get('age') < 18):
            raise serializers.ValidationError({'error':'Age cannot be less than 18.'})
        
        if 'marks' in data and (data.get('marks') < 0 or data.get('marks') > 100):
            raise serializers.ValidationError({'error':'Marks Should between 0 to 100'})

        return data