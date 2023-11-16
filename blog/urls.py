from django.urls import path, include
from .views.blog_views import Index, DetailBlogView
from .views.contact_views import ContactFormView
from .views.category_view import PostByCategoryView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('blog/<str:slug>/', DetailBlogView.as_view(), name='blog_detail'),
    path('category/<str:slug>/', PostByCategoryView.as_view(), name='category_slug'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
