from django.shortcuts import render_to_response

from lib.utils import render_to

from blog.models import Entry


@render_to('blog/index.html')
def blog_index(request):
    latest_entries = Entry.objects.filter(status=Entry.Status.LIVE).order_by('-publish')
    return locals()
