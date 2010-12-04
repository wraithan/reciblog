from django.shortcuts import render_to_response
from lib.utils import render_to, get_or_none
from blog.models import Entry


@render_to('blog/index.html')
def blog_index(request):
    latest_entries = Entry.objects.filter(status=Entry.Status.LIVE).order_by('-publish')
    return locals()


@render_to('blog/entry_detail.html')
def entry_detail(request, year, month, day, slug):
    entry = get_or_none(model=Entry, publish__year=year, publish__month=month, publish__day=day, slug=slug)
    return locals()
