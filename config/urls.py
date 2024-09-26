from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),     
    
    # Local apps    
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]

if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()