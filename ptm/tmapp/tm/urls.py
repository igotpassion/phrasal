from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tm.views',
    # PTM translation manager (TM) app
    url(r'^$', 'index'),
    url(r'^(?P<src_id>\d+)/$', 'history'),
    url(r'^training/$', 'training'),
    url(r'^tr/$', 'tr'),
)
