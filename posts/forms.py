from django import forms
import django_filters
import itertools
from . import models


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ('label','title','body')

class PostFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(lookup_expr='icontains', field_name='body')


    class Meta:
        model = models.Post
        fields = ['label']
