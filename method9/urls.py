from django.urls import path, include
from rest_framework import routers
from method9.views import SubjectViewSet

router9 = routers.DefaultRouter()
router9.register('subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router9.urls))   
]