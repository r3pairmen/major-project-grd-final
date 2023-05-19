from django.contrib import admin
from django.urls import path, include
from scanner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scanner/', include('scanner.urls')),
]
