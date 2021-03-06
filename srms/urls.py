"""srms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.views import generic
from material.frontend import urls as frontend_urls

admin.site.site_header = settings.ADMIN_SITE_HEADER
urlpatterns = [

                  url(r'^erp/', include('erp.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^report_builder/', include('report_builder.urls')),
                  url(r'^avatar/', include('avatar.urls')),
                  url(r'^$', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
                  url(r'', include(frontend_urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
