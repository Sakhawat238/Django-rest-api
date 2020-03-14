from django.urls import path, include
from rest_framework import routers
from method9.views import SubjectViewSet, StudentViewSet

router9 = routers.DefaultRouter()
router9.register('subjects', SubjectViewSet)
router9.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router9.urls))   
]