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
    (r'^$', 'app4u.views.index'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^app4u/$', homey),
    url(r'^app4u/admin_login/$', admin_loginn), 
    url(r'^app4u/user_login/$', user_loginn),
    url(r'^app4u/admin_login/admin_homepage/$', admin_home),
    url(r'^app4u/admin_login/admin_homepage/done/$', select),
    url(r'^app4u/admin_login/admin_homepage/testing/$', user_captcha), 
    url(r'^app4u/admin_login/admin_homepage/done/real_selected$', include('app4u.urls')), 
    url(r'^app4u/admin_login/admin_homepage/done/fake_selected$', include('app4u.urls1')), 
    url(r'^app4u/admin_login/admin_homepage/logout_page/$', logout_page),
    url(r'^app4u/admin_login/admin_homepage/test/$', test),
    url(r'^app4u/user_login/user_captcha/$', user_captcha),
    
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

