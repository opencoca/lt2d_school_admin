from .models import Classroom, Teacher, App
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['name', 'logo', 'iframe']

class ClassroomSerializer(serializers.HyperlinkedModelSerializer):
    teacher_set = TeacherSerializer(many=True)
    app_set = AppSerializer(many=True)

    class Meta:
        model = Classroom
        fields = ['name', 'pub_date', 'breakout_rooms', 'order', 'teacher_set', 'taught_by', 'app_set']
