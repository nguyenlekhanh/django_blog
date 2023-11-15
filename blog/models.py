from django.db import models
import uuid
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class Category(BaseModel):
    
    name = models.CharField(max_length=200, null=True)
    order = models.IntegerField(default=0)
    parent = models.IntegerField(default=0)


    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Post(BaseModel):
    title = models.CharField(max_length=300, null=True)
    slug = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null=True)
    description = models.TextField(null=True)
    content = HTMLField()
    post_id = models.CharField(max_length=255, null=False, default=uuid.uuid4().__str__())
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post', null=True)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title