"""colombia_birds URL Configuration."""

#Django
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('observer.urls', 'observer'), namespace='observer')),
]
