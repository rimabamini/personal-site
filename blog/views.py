from django.shortcuts import render
from blog.models import Post


def blog_index(request):
    # import post model, import Queryset containing all posts in database
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

# take a category name and query the Post database for all posts 
def blog_category(request, category):
    # filter post that contain category name corresponding to argument
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

# requires form, takes primary key value as argument to retrieve object 
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_detail.html", context)