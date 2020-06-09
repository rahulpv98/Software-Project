from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required(login_url= '/sign_in')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request,'blog/post_edit.html',{'form':form})

@login_required(login_url= '/sign_in')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def topic_dis(request):
    posts = Post.objects.filter()
    title = []
    for i in posts:
        title.append(i.topic)
    title = list(set(title))
    return render(request, 'blog/topic_dis.html', {'title':title})

def topic_list(request):
    posts = Post.objects.filter()
    topic_post = []
    if request.method == "POST":
        topic = request.POST.get('topic_name').strip()
        for i in posts:
            if topic == i.topic:
                topic_post.append(i)
        return render(request, 'blog/topic_list.html', {'topic_post':topic_post})
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

def search_list(request):
    posts = Post.objects.filter()
    title_post = []
    if request.method == "POST":
        title = request.POST.get('word_search').strip()
        for i in posts:
            if title in (i.title):
                title_post.append(i)
        return render(request, 'blog/search_list.html', {'title_post':title_post})
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'blog/sign_up.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request,'blog/sign_in.html',{"form":form})

@login_required(login_url= '/sign_in')
def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

def post_delete(request, pk):
    post=get_object_or_404(Post, pk=pk)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post.delete()
    return redirect('/content')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comments = Comment.objects.filter()
    comment.delete()
    return redirect('/content')