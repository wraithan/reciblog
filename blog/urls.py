from django.conf.urls.defaults import patterns, url
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.blog_index, name='blog_index'),
)
