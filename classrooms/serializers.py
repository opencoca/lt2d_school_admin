from .models import Room, Classroom, Teacher, App, Platform
from rest_framework import serializers

class CustomSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['name', 'logo', 'iframe']

class ClassroomSerializer(CustomSerializer):
    teacher_set = TeacherSerializer(many=True)
    app_set = AppSerializer(many=True)
    platform = PlatformSerializer(read_only=True)

    class Meta:
        model = Classroom
        fields = '__all__'
        extra_fields = ['name','meet', 'taught_by']

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    classroom = ClassroomSerializer(read_only = True)
    class Meta:
        model = Room
        fields = ['name','route','meet','classroom']
