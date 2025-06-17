# forum/views.py
from django.shortcuts import render, redirect
from .models import AnonymousPost
from .forms import PostForm
from django.utils import timezone

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
