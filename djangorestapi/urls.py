from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/m1/',include('method1.urls')),
    path('api/m2/',include('method2.urls'))
]
