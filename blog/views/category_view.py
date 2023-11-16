from typing import Any
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import View
from django.urls import reverse, reverse_lazy
from ..models import Category, Post
from django.views.generic import ListView, DetailView
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostByCategoryView(ListView):
    template_name = 'blog/post_by_category.html'  # Update with your actual template
    context_object_name = 'post_list'

    def get(self, request, *args, **kwargs):
        # Retrieve the category based on the slug from the URL
        category_slug = kwargs['slug']

        # Use filter().first() to avoid MultipleObjectsReturned exception
        category = Category.objects.filter(slug=category_slug).first()

        # If category is None, redirect to the home page
        if category is None:
            return redirect('index')  # 'home' is the name of your home page URL pattern

        # Set the category in the context for the template
        self.category = category

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # Retrieve the posts related to the category
        category_id = self.category.id

        
        # posts = Post.objects.filter(category=self.category)

        
        with connection.cursor() as cursor:
            cursor.execute(f'''
                SELECT blog_post.*, blog_category.name AS category_name, blog_category.slug AS category_slug
                FROM blog_post
                LEFT JOIN blog_category ON blog_post.category_id = blog_category.id
                WHERE blog_post.category_id = 1
                ORDER BY blog_post.updated_at DESC
            ''')
            columns = [col[0] for col in cursor.description]
            queryset = [dict(zip(columns, row)) for row in cursor.fetchall()]

        p = Paginator(queryset, 10)

        page_num = self.request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        queryset = page
        return queryset
    