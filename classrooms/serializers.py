from .models import Room, Classroom, Teacher, App
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['name', 'logo', 'iframe']

class ClassroomSerializer(serializers.ModelSerializer):
    teacher_set = TeacherSerializer(many=True)
    app_set = AppSerializer(many=True)

    class Meta:
        model = Classroom
        fields = '__all__'

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    classroom = ClassroomSerializer(read_only = True)
    class Meta:
        model = Room
        fields = ['name','route','meet','classroom']
