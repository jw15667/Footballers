from django.contrib import admin
from django.urls import re_path, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [ 
                re_path(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
                re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='blog/post.html'))            ]
