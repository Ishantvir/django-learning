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
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'Name Should not contain numbers.'})

        if data['age'] < 18:
            raise serializers.ValidationError({'error':'Age cannot be less than 18.'})
        
        if data['marks'] < 0 or data['marks'] > 100:
            raise serializers.ValidationError({'error':'Marks Should between 0 to 100'})

        return data