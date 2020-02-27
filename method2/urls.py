from django.urls import path
from method2.views import SchoolList, SchoolDetails, SchoolCreate, SchoolUpdate

urlpatterns = [  
    path('schools/', SchoolList, name="schools_list"),
    path('schools/<int:id>/', SchoolDetails, name="school_details"),
    path('schools/add/', SchoolCreate, name="school_create"),
    path('schools/edit/<int:id>/', SchoolUpdate, name="school_update")   
]


