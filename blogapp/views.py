# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    blog = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'blogs':blog, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':blog_detail})

def write(request):
    return render(request, 'write.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    messages.success(request, '작성되었습니다!')
    return redirect('/' + str(blog.id))

def map(request):
    return render(request, 'map.html')
    