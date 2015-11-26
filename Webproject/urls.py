"""Webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
""" 
from django.conf.urls import patterns,include, url
from app4u.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = patterns('',
    # (r'^app4u/', include('app4u.urls')),
    (r'^$', 'app4u.views.index'),
    (r'^admin/', include(admin.site.urls)),
#     url(r'^$', homey),
    url(r'^app4u/$', homey),
    url(r'^app4u/admin_login/$', admin_loginn), 
    url(r'^app4u/admin_login/done/$', include('app4u.urls')), 
    # url(r'^app4u/admin_login/$',include('app4u.urls')),
    # url(r'^app4u/user_login/$',user_loginn),
    url(r'^app4u/user_login/$',include('app4u.urls2')),
#     # url(r'^accounts/login/$', 'django.contrib.auth.views.homey'), # If user is not login it will redirect to login page
#     url(r'^register/$', register),
#     url(r'^register/success/$', register_success),
#     url(r'^admin_login/$', admin_loginn),
#     url(r'^user_login/$', user_loginn),
#     url(r'^user_login/homey$', homey),
#      url(r'^homey/user_login/$', user_loginn),
#     # url(r'^home/$', home),
#     url(r'^homey/$', homey),
#     url(r'^homey/admin_login/$', admin_loginn),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

