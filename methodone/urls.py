from django.urls import path, include
from .views import SubjectViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('', SubjectViewSet)

urlpatterns = [
    # path('subjects/', include(router.urls))   
    path('subjects/', SubjectViewSet, name="subjects_list") 
]
