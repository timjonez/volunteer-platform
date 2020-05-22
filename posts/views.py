from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from functools import reduce
import operator
from django.db.models import Q
from .models import Post, Category
from .forms import PostForm, PostFilter
from django.http import HttpResponseForbidden

from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, TemplateView,
                                  DetailView, ListView)

# Create your views here.
decorators = [user_passes_test(lambda u: u == obj.user)]

class CreatePostView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'posts/post_detail.html'
    form_class = PostForm
    model = Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


class MyPermissionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)


class UpdatePostView(MyPermissionMixin, UpdateView):
    redirect_field_name = 'posts/post_detail.html'
    form_class = PostForm
    model = Post

    def test_func(self):
        return self.request.session.get('issuer_pk', None) is not None



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')


def post_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.all().order_by('-created_date'))
    return render(request, 'posts/post_list.html',{'filter':f})




class PostDetailView(DetailView):
    model = Post
