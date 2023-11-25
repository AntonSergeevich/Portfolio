from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
def blogPage(request):
    posts = Post.objects.all()
    context = {'posts': posts, }
    return render(request, 'base/blog.html', context)


def postPage(request, pk):
    post = Post.objects.get(id=pk)
    count = post.comment_set.count()
    comments = post.comment_set.all().order_by('-created')
    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = post
            comment.name = request.user
            comment.save()
            messages.success(request, 'Комментарий оставлен ☺')
    form = CommentForm()
    context = {'post': post, 'count': count, 'comments': comments, 'form': form}
    return render(request, 'base/detail_blog.html', context)
