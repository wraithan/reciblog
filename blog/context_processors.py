from blog.models import Category, Entry


def sidebar(request):
    sidebar_categories = Category.objects.all()
    sidebar_latest_entries = Entry.objects.all()[:5]
    return locals()
