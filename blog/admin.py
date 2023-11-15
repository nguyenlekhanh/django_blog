from django.contrib import admin

# Register your models here.

from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'created_at', 'updated_at')
    #use in add new or edit
    #fields = ['name', 'order', 'parent']

#admin.site.register(Category)
admin.site.register(Post)