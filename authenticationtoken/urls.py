from django.urls import path
from authenticationtoken.views import GenerateToken, SubjectTokenAuthViewset, SubjectDetailTokenAuthGenericview
from rest_framework.authtoken import views


urlpatterns = [
    path('generate-token/', GenerateToken, name="token_generator"),
    path('api-token-auth/',views.obtain_auth_token),
    path('subjects/', SubjectTokenAuthViewset, name="subject_tokenauth_viewset"),
    path('subjects/<int:id>/', SubjectDetailTokenAuthGenericview.as_view(), name="subject_detail_tokenauthgeneric_view")
]