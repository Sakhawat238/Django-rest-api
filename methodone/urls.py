from django.urls import path, include
from methodone.views import SubjectList, SubjectDetails, SubjectCreate, SubjectUpdate

urlpatterns = [  
    path('subjects/', SubjectList, name="subjects_list"),
    path('subjects/<int:id>/', SubjectDetails, name="subject_details"),
    path('subjects/add/', SubjectCreate, name="subject_create"),
    path('subjects/edit/<int:id>/', SubjectUpdate, name="subject_update")   
]
