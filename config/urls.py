from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('secure-admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),     # Enable 'ckeditor' editor
    path('__debug__/', include('debug_toolbar.urls')),    # Enable 'django-debug-toolbar'
    path('silk/', include('silk.urls', namespace='silk')),    # Enable 'django-silk'
    path('watchman/', include('watchman.urls')),    # Enable 'django-watchman'

    path('shipping/', include('shipping.urls')),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
