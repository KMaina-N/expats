from django.shortcuts import render, redirect
from .models import*
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
# https://github.com/legionscript/socialnetwork/blob/tutorial11/social/views.py
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html', {})


def home(request):
    print(request.user)
    logged_in = request.user
    print(logged_in)
    posts = Post.objects.all().order_by('-created_on')
    # posts = Post.objects.all().order_by('-created_on')
    return render(request, 'home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        print(request.user)
        post = request.POST.get('post')
        author = request.user
        Post.objects.create(body=post, author=author)
        return redirect('home')
    # return render(request, 'add_post.html', {})

def add_like(request, pk):
    post = Post.objects.get(id=pk)
    post.likes.add(request.user)
    return redirect('home')

def add_comment(request, pk):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        author = request.user.id
        post = Post.objects.get(id=pk)
        Comment.objects.create(comment=comment, author_id=author, post=post)
        return redirect('home')
    return render(request, 'add_comment.html', {})