from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/m1/',include('method1.urls')),
    path('api/m2/',include('method2.urls')),
    path('api/m3/',include('method3.urls')),
    path('api/m4/',include('method4.urls')),
    path('api/m5/',include('method5.urls')),
    path('api/m6/',include('method6.urls'))
]
