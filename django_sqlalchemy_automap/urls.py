from django.contrib import admin
from django.urls import path, include
from myapp import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
