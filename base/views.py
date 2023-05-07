from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/home.html', context)

def posts(request):
    return HttpResponse('posts')


def post(request):
    return HttpResponse('post')

def profile(request):
    return HttpResponse('profile')