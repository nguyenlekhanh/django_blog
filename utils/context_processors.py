from blog.models import Category, Post
from django.db.models import Count

def category_processor(request):
    categoryMenu = [1, 2]
    categories = Category.objects.filter(id__in=categoryMenu).annotate(total_posts=Count('post'))  # Adjust this query based on your model
    return {'categories': categories}


def new_post(request):
    categoryMenu = [1, 2]
    new_posts = Post.objects.all().order_by('-created_at')[:5]  # Adjust this query based on your model
    return {'new_posts': new_posts}