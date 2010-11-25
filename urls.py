from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('reciblog.blog.urls')),
    (r'^admin/', include(admin.site.urls)),
)
