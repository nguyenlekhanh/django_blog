# from django.shortcuts import render
# from django.views import View
# from .models import Category, Post
# from django.views.generic import ListView, DetailView


# class Index(ListView):
#     model = Post
#     paginate_by = 2
#     context_object_name = 'post_list'
#     queryset = Post.objects.all().order_by('-updated_at')
#     template_name = 'blog/index.html'
#     #return render(request, 'blog/index.html', context)
#     # def get(self, request):
#     #     categories = Category.objects.all()
#     #     context = {'categories': categories}


#     #     return render(request, 'blog/index.html', context)


# class DetailBlogView(DetailView):
#     model = Post
#     template_name = 'blog/blog_post.html'
#     context_object_name = 'post_list'
#     queryset = Post.objects.all().order_by('-updated_at')
    
#     #return render(request, 'blog/index.h