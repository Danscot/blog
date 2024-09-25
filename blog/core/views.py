
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def main(request):

    posts = Post.objects.all().order_by('-created_at')  #

    return render(request, 'blog.html', {'posts':posts})

def more(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    return render(request, 'content.html', {'post': post})
