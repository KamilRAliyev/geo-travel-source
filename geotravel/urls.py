"""geotravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, resolve, reverse
from django.conf import settings
from django.conf.urls.static import static
from froala_editor import views


urlpatterns = [
    path('geomin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path("", include("geotravel_app.urls")),
    path("tours/", include("tours.urls")),
    path("guides/", include("guides.urls")),
    path('transport/', include('transport.urls')),
    prefix_default_language=False,
)

urlpatterns += [
    path('geotranslate/', include('rosetta.urls')),
]

handler404 = 'geotravel_app.views.error_404'

# not for production
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)