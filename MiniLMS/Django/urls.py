"""
URL configuration for Mini LMS project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# Template views
def index(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def lessons(request):
    return render(request, 'lessons.html')

def assignments(request):
    return render(request, 'assignments.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/courses/', include('courses.urls')),
    # HTML template URLs
    path('', index, name='index'),
    path('courses/', courses, name='courses'),
    path('lessons/', lessons, name='lessons'),
    path('assignments/', assignments, name='assignments'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
