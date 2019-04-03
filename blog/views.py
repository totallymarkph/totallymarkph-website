from django.shortcuts import render
from blog.models import Blog


def blog_index(request):
    posts = Blog.objects.all().order_by('-date_created')
    context = {
        'posts': posts,
    }
    return render(request, "blog/blog_index.html", context)

def blog_detail(request, pk):
    post = Blog.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, "blog/blog_detail.html", context)