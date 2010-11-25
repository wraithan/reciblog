from django.shortcuts import render_to_response


def blog_index(request):
    return render_to_response('blog/index.html')
