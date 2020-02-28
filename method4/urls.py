from django.urls import path
from method4.views import SubjectViewset, SubjectDetailViewset

urlpatterns = [
    path('subjects/', SubjectViewset, name="subject_viewset_apiview"),
    path('subjects/<int:id>/', SubjectDetailViewset, name="subject_detailviewset_apiview")
]