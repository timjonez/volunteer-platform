from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('chuch/<int:pk>/', views.ChurchDetail.as_view(), name='church_detail'),
    path('chuch/<int:pk>/contact/', views.emailView, name='contact')
    #path('chuch/<int:pk>/contact/', views.ChurchContact.as_view(), name='church_contact')
]
