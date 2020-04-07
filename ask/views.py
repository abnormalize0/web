from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Tag
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import PostForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'ask/post_list.html', {'posts': posts})

@login_required(login_url="/ask/login")
def ask_create(request):
    return render(request,"ask/ask_create.html")

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'ask/ask_create.html', {'form': form})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'ask/tags.html', {'tags': tags})

def tag_detail(request, slug):
    tags = Tag.objects.get(slug__iexact=slug)
    return render(request, 'ask/tag_detail.html', {'tags': tags})

def question_detail(request, slug):
    #todo
    return render(request, 'ask/question_detail.html')

def hot_questions(request):
    #todo
    return render(request, 'ask/hot.html', {'posts': posts})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request,'ask/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request,'ask/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('post_list')

def paginate(objects_list, request, per_page=10):
    # do smth with Paginator, etc…
    return page