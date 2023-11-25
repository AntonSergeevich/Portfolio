from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Category


def coursesAllPage(request):
    posts_all = Category.objects.all()
    context = {
        'posts_all': posts_all,
        'cat_selected': 0,
        }
    return render(request, 'base/courses.html', context=context)


def show_course(request, post_slug):
    post = get_object_or_404(Course, slug=post_slug)
    context = {
        'post': post,
        'cat_selected': post.cat_id,
        }
    return render(request, 'base/courses.html', context=context)


def show_category(request, cat_id):
    posts = Course.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'cat_selected': cat_id,
               }
    return render(request, 'base/courses.html', context=context)
