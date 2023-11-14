from django.shortcuts import render
from django.views import View
from .models import Category

# Create your views here.
class Index(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}


        return render(request, 'blog/index.html', context)
