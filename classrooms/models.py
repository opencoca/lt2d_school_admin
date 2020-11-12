import datetime

from django.db import models
from dataclasses import dataclass, field
from django.utils import timezone

class IntegerRangeField(models.IntegerField):
    """
    Allows for integers fields with custom ranges.

    example: size = fields.IntegerRangeField(min_value=1, max_value=5)
    """
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Room(models.Model):
    """
    This represents a virtual room
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    route = models.CharField(max_length=20, default='meet', editable=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        verbose_name_plural = "0. Rooms"

    def __str__(self):
        return "%s Room" % self.name


class Classroom(models.Model):
    """
    This represents a virtural classroom
    """
    room = models.OneToOneField(
        Room,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    pub_date = models.DateTimeField('date published')
    breakout_rooms = IntegerRangeField(min_value=1, max_value=5)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        verbose_name_plural = "1. Class Rooms"

    def __str__(self):
        return self.room.name

    def name(self):
        return self.room.name

    def address(self):
        return self.room.address

    def taught_by(self):
        self.short_description = 'Teacher(s)'
        return ", ".join([teacher.first_name for teacher in self.teacher_set.all()])


    def recent_class(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=180)

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    classes = models.ManyToManyField(Classroom, blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        verbose_name_plural = "2. Teachers"

    def __str__(self):
        return self.first_name

class App(models.Model):
    """
    Classroom apps are powered by iframes
    """
    name = models.CharField(max_length=200)
    iframe = models.URLField(max_length=200)
    logo   = models.URLField(max_length=200)
    classes = models.ManyToManyField(Classroom, blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        verbose_name_plural = "3. Apps"

    def __str__(self):
        return self.name
