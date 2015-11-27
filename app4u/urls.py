from django.conf.urls import patterns,include, url

urlpatterns = patterns('app4u.views',
	url(r'^$', 'list', name='list'),
  )
