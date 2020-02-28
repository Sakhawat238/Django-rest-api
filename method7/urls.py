from django.urls import path, include
from rest_framework import routers
from method7.views import SubjectViewSet

router = routers.DefaultRouter()
router.register('', SubjectViewSet, basename='subjects')

urlpatterns = [
    path('subjects/', include(router.urls))   
]
