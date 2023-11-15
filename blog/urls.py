from django.urls import path, include
from .views.blog_views import Index, DetailBlogView
from .views.contact_views import ContactFormView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('blog/<str:slug>/', DetailBlogView.as_view(), name='blog_detail'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
