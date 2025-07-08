# forum/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import AnonymousPost, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    form = PostForm()
    if request.method == 'POST':
        if 'submit_post' in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.created_at = timezone.now()
                post.save()
                return redirect('home')

        elif 'submit_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            post_id = request.POST.get('post_id')
            post = AnonymousPost.objects.get(id=post_id)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.created_at = timezone.now()
                comment.save()
                return redirect('home')
    else:
       comment_form  = CommentForm()

    comment_form = CommentForm()
    posts = AnonymousPost.objects.order_by('-created_at')

    return render(request, 'home.html', {
        'form': form,
        'posts': posts,
        'comment_form': comment_form
    })


def like_post(request, post_id):
    post = get_object_or_404(AnonymousPost, pk=post_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def post_detail(request, post_id):
    post = get_object_or_404(AnonymousPost, pk=post_id)
    comments = post.comments.order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_at = timezone.now()
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'form': form,
        'comments': comments
    })
