from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('simpleblog.urls')),
    path('geeks/',include('geeks.urls')),
    path('core/',include('core.urls', namespace='my_core')),
    # the original should listed first
    # if django see undefine  url path then the local will be used
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns