from django.urls import path, include
from rest_framework import routers
from method10.views import StudentNestedViewSet, TeacherNestedViewSet

router = routers.DefaultRouter()
router.register('students', StudentNestedViewSet)
router.register('teachers', TeacherNestedViewSet)

urlpatterns = [
    path('', include(router.urls))   
]