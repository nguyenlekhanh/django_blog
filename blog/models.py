from django.db import models
# import uuid
# from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=200, null=True)
    order = models.IntegerField(default=0)
    parent = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        