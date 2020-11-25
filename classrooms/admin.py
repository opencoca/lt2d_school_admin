from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django_reverse_admin import ReverseModelAdmin
from .models import *

class TeacherInline(admin.TabularInline):
    model= Teacher.classes.through
    extra = 0

class AppInline(admin.TabularInline):
    model = App.classes.through
    extra = 0

#@admin.register(Room)
#class RoomAdmin(SortableAdminMixin, admin.ModelAdmin):
#    model = Room

@admin.register(Classroom)
class ClassroomAdmin(SortableAdminMixin, ReverseModelAdmin, admin.ModelAdmin):
    model = Classroom
    inline_type = 'tabular'
    inline_reverse = [('room', {'fields': ['name','meet']})]
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
