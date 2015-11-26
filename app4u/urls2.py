from django.conf.urls import patterns,include, url

urlpatterns = patterns('app4u.views',
	# url(r'^$', 'list', name='list'),
    # url(r'^list/$', 'list', name='list'),

	url(r'^$', 'listprint', name='listprint'),
    # url(r'^$', 'listprint', name='listprint'),
    # url(r'^$', 'django.contrib.auth.views.login'),
  )
