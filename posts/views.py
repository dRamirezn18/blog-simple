from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):
  posts = Post.objects.all()
  return render(request, "post/post.html", {"posts": posts})

def post(request, pk):
  post = get_object_or_404(Post, id=pk)
  return render(request, "post/post_detail.html", {"post": post})