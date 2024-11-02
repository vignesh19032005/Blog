from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'posts': posts,
        'page_title': "Vignesh's Blog - Home"
    }
    return render(request, 'posts/index.html', context)  

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'page_title': f"{post.title} - Vignesh's Blog"
    }
    return render(request, 'posts/post_detail.html', context)  
