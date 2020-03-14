from django.urls import path
from method11.views import StudentListAPIView, StudentRetrieveAPIView

urlpatterns = [
    path('students/', StudentListAPIView.as_view(), name="student_list_api_view"),   
    path('students/<int:id>/', StudentRetrieveAPIView.as_view(), name="student_retrieve_api_view")
]