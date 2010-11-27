from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('reciblog.blog.urls')),
    url(r'^about$', direct_to_template, {'template': 'about.html'}, name='about'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG == True:
    print 'test'
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        )
