from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Classroom, Teacher, App

class TeacherInline(admin.TabularInline):
    model= Teacher.classes.through
    extra = 0

class AppInline(admin.TabularInline):
    model = App.classes.through
    extra = 0

@admin.register(Classroom)
class ClassroomAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Classroom
    list_display = ('name',  'breakout_rooms', 
                    'taught_by', 'recent_class')
    inlines = [
        TeacherInline,
        AppInline
    ]

@admin.register(App)
class AppAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = App

@admin.register(Teacher)
class TeacherAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Teacher
