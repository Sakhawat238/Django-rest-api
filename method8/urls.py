from django.urls import path, include
from rest_framework import routers
from method8.views import SubjectViewSet

router8 = routers.DefaultRouter()
router8.register('subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router8.urls))   
]