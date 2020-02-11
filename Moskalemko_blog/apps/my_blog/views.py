from django.shortcuts import render
from django.http import HttpResponse
import random
from Moskalemko_blog.apps.my_blog.models import Post, Keywords
# Create your views here.




def index(requset):
    keywords_list = Keywords.objects.all()
    post_list = Post.objects.all()
    context = {
        'posts':post_list,
        'keywords':keywords_list
    }
    return render(requset, "index.html", context)

def post(requset, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post':post,
    }
    return render(requset, "post.html", context)

def about(requset):
    context = {

    }
    return render(requset, "about.html", context)

def contacts(requset):
    context = {

    }
    return render(requset, "contacts.html", context)