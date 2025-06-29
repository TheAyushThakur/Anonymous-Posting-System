# forum/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import AnonymousPost
from .forms import PostForm
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    posts = AnonymousPost.objects.order_by('-created_at')
    return render(request, 'home.html', {'form': form, 'posts': posts})

def like_post(request, post_id):
    post = get_object_or_404(AnonymousPost, pk = post_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

