from dselector import Parser
from blog import views


parser = Parser()
url = parser.url
patterns = parser.patterns

urlpatterns = patterns(
    '',
    url(r'', views.blog_index, name='index'),
    url(r'blog/{year:year}/{month:digits}/{day:day}/{slug:slug}/', views.entry_detail, name='entry_detail'),
)
