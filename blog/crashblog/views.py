from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'crashblog/detail.html', {'post': post, 'form': form})

