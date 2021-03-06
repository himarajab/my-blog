from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns 

from django.contrib import admin
from django.urls import path,include

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('',include('simpleblog.urls')),
    # mine is the first cause easily override the common ones
    path('members/',include('members.urls',namespace="accounts")),
    path('members/',include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False
 )  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns