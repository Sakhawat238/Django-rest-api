from django.urls import path
from method6.views import SubjectGenericview, SubjectDetailGenericview


urlpatterns = [
    path('subjects/', SubjectGenericview.as_view(), name="subject_generic_view"),
    path('subjects/<int:id>/', SubjectDetailGenericview.as_view(), name="subject_detailgeneric_view")
]