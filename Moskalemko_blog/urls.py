"""Moskalemko_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from  django.urls import include
from Moskalemko_blog.apps.my_blog.views import index, about, contacts, post, author



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('contacts/', contacts),
    re_path(r'^post/(?P<post_id>\d+)$', post,  name='post'),
    re_path(r'^author/(?P<author_id>\d+)$', author,  name='author'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))


]
