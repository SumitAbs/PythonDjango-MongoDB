from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# App-specific routing for MongoDB User Management
urlpatterns = [
    # Pages
    path('', views.home, name='home'),  
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_create, name='user_create'),
    
    # Logic for Edit and Delete (Required for your Template)
    path('users/edit/<int:pk>/', views.user_update, name='user_update'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]