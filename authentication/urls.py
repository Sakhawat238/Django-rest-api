from django.urls import path
from authentication.views import SubjectAuthViewset, SubjectDetailAuthGenericview


urlpatterns = [
    path('subjects/', SubjectAuthViewset, name="subject_auth_viewset"),
    path('subjects/<int:id>/', SubjectDetailAuthGenericview.as_view(), name="subject_detailauthgeneric_view")
]