from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/m1/',include('method1.urls')),
    path('api/m2/',include('method2.urls')),
    path('api/m3/',include('method3.urls')),
    path('api/m4/',include('method4.urls')),
    path('api/m5/',include('method5.urls')),
    path('api/m6/',include('method6.urls')),
    path('api/m7/',include('method7.urls')),
    path('api/m8/',include('method8.urls')),
    path('api/m9/',include('method9.urls')),
    path('api/auth/',include('authentication.urls')),
    path('api/tokenauth/',include('authenticationtoken.urls'))
]
