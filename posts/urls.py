from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.CreatePostView.as_view(), name='post_new'),
    path('<int:pk>/edit/', views.UpdatePostView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

]
