from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import CommentForm

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, status=Post.ACTIVE, slug=slug)
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

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'crashblog/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'crashblog/search.html', {'posts': posts, 'query': query})