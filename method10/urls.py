from django.urls import path
from method10.views import StudentNestedView, TeacherNestedView


urlpatterns = [
    path('students/', StudentNestedView.as_view(), name="student_nested_view"),
    path('teachers/', TeacherNestedView.as_view(), name="teacher_nested_view")
]

