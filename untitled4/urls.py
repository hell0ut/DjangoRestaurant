from django.contrib import admin
from django.urls import path,include
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('menu/',include('menu.urls')),
    path('info/',include('info.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)