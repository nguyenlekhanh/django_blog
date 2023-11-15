from typing import Any
from django.shortcuts import render
from django.views import View
from ..models import Category, Post
from django.views.generic import ListView, DetailView


class Index(ListView):
    model = Post
    paginate_by = 2
    context_object_name = 'post_list'
    queryset = Post.objects.all().order_by('-updated_at')
    template_name = 'blog/index.html'


class DetailBlogView(DetailView):
    model = Post
    template_name = 'blog/blog_post.html'
    context_object_name = 'post_list'
    queryset = Post.objects.all().order_by('-updated_at')

    #the quick way to add some data to context
    #and return to view
    def get_context_data(self, *args, **kwargs):
        context = super(DetailBlogView, self).get_context_data(*args, **kwargs)
        post = Post.objects.get(slug=self.kwargs.get('slug'))
        context['post'] = post
        return context
    
    #return render(request, 'blog/index.h