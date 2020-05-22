from django.db import models
from django.utils import timezone
from django.urls import reverse

from users.models import CustomUser
# Create your models here.

class Category(models.Model):
    category_item = models.CharField(max_length=100, help_text='Category')

    def get_absolute_url(self):
        return reverse('posts:post_list')

    def __str__(self):
        return self.category_item

class Post(models.Model):
    user = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    label = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('posts:post_list')


    def __str__(self):
        return self.title
