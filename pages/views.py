from django.shortcuts import render, redirect
from .models import Post
from .forms import ContactForm, PostForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
  context = {'name': 'Isaac'}
  return render(request, 'pages/home.html', context)

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
  else:
    form = ContactForm()
  return render(request, 'pages/contact.html', {'form': form})

@login_required
def about(request):
  return render(request, 'pages/about.html')

@login_required
def blog(request):
  posts = Post.objects.filter(author=request.user).order_by('-published_date')
  return render(request, 'pages/blog.html', {'posts' : posts})

def post_detail(request, slug):
  post = Post.objects.get(slug=slug)
  return render(request, 'pages/post_detail.html', {'post': post})


@login_required
def create_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      print('Form is valid', post)
      post.author = request.user
      post.save()
      print('Post really saved')
      messages.success(request, "Post created successfully!")
      return redirect('blog')
    else:
      messages.error(request, "There was a problem with the form.")
  else:
    form = PostForm()
  return render(request, 'pages/post_form.html', {'form': form})

@login_required
def edit_post(request, slug):
  post = Post.objects.get(slug=slug)
  form = PostForm(request.POST or None, instance=post)
  if form.is_valid():
    form.save()
    return redirect('post_detail', slug=post.slug)
  return render(request, 'pages/edit_post.html', {'form': form})

@login_required
def delete_post(request, slug):
  post = Post.objects.get(slug=slug)
  if request.method == 'POST':
    post.delete()
    return redirect('blog')
  return render(request, 'pages/post_confirm_delete.html', {'post': post})

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserCreationForm()
  return render(request, 'registration/register.html', {'form': form})



