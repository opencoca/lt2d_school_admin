from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from django.core import serializers
from django.http import HttpResponse

from .models import Classroom, Teacher, App
from .serializers import ClassroomSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows classrooms to be viewed or edited.
    """
    queryset = Classroom.objects.all().order_by('-pub_date')
    serializer_class = ClassroomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def list(request):
  '''Returns a list of all classrooms and their details'''
  classrooms = Classroom.objects.all()
  if 'application/json' in request.META.get('HTTP_ACCEPT'):
    return HttpResponse(serializers.serialize("json", classrooms), content_type='application/json')
  else:
    #return HttpResponse("400 Bad Request")
    return HttpResponse(serializers.serialize("json", classrooms), content_type='application/json')
