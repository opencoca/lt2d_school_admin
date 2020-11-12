from django.contrib import admin
from django.urls import include, path
from classrooms.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)

admin.site.site_header = 'Out Site Admin Panel'
admin.site.site_title = 'Our Site Title'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
