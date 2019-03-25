from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Count
import pdb

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'user' : request.user,
        'users_posts_count' : request.user.posts().count(),
        'posts': posts,
        'comment_form': CommentForm(),
    }
    return render(request, 'posts/home.html', context)


def new(request):
    context = {
            'form': PostForm(initial={'user': request.user})
    }
    return render(request, 'posts/new.html', context)


def create(request):
    context = {}
    if request.method == "POST":
       form = PostForm(request.POST, request.FILES or None)
       if form.is_valid():
           form.save()
    return redirect('home')


def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if 'id' is not None:
        context = {
            'post': post,
            'form': PostForm(instance=post)
        }
        return render(request, 'posts/edit.html', context)


def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()

        return redirect('home')


def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.delete()

        return redirect('home')
    return redirect('home')



def comment_create(request, post_id):
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.post = get_object_or_404(Post, pk=post_id)
        comment.body = request.POST.get('body')
        comment.save()
        return redirect('home')