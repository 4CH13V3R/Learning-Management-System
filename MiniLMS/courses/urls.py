from django.urls import path
from .views import (
    CourseListCreateView, 
    CourseDetailView, 
    LessonListCreateView,
    AssignmentListCreateView,
    SubmissionListCreateView,
    MySubmissionsView
)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course_list_create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('lessons/', LessonListCreateView.as_view(), name='lesson_list_create'),
    path('assignments/', AssignmentListCreateView.as_view(), name='assignment_list_create'),
    path('submissions/', SubmissionListCreateView.as_view(), name='submission_list_create'),
    path('my-submissions/', MySubmissionsView.as_view(), name='my_submissions'),
]
