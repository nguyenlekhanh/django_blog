from typing import Any
from django.shortcuts import render
from django.views import View
from ..models import Category, Post
from django.views.generic import ListView, DetailView
from django.db import connection

class Index(ListView):
    model = Post
    paginate_by = 2
    context_object_name = 'post_list'
    #queryset = Post.objects.all().order_by('-updated_at')
    template_name = 'blog/index.html'

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT blog_post.*, blog_category.name AS category_name, blog_category.slug AS category_slug
                FROM blog_post
                LEFT JOIN blog_category ON blog_post.category_id = blog_category.id
                ORDER BY blog_post.updated_at DESC
            ''')
            columns = [col[0] for col in cursor.description]
            queryset = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return queryset


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