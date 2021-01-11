from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include, path
from classrooms.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)

admin.site.site_header = 'Out Site Admin Panel'
admin.site.site_title = 'Our Site Title'

urlpatterns = [
    path('', include(router.urls)),
    path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('studio/', include('studio.urls')),
    path('polls/', include('polls.urls')),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),
]

#Adding media files 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
