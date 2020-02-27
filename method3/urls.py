from django.urls import path
from method3.views import SubjectViewset, SubjectDetailViewset

urlpatterns = [
    path('subjects/', SubjectViewset, name="subject_viewset"),
    path('subjects/<int:id>/', SubjectDetailViewset, name="subject_detail_viewset")
]