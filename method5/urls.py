from django.urls import path
from method5.views import SubjectApiview, SubjectDetailApiview


urlpatterns = [
    path('subjects/', SubjectApiview.as_view(), name="subject_api_view"),
    path('subjects/<int:id>/', SubjectDetailApiview.as_view(), name="subject_detailapi_view")
]