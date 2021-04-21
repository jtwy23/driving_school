from django.urls import path
from . import views


urlpatterns = [
    # Index
    path('', views.index, name='index'),
    # All lessons
    path('all_lessons', views.all_lessons, name='all_lessons'),
    # Searching for products
    path('product_search', views.product_search, name='product_search'),
    # User profile
    path('profile', views.profile, name='profile'),
    # User profile edit
    path('edit_profile', views.edit_profile, name='edit_profile'),
    # User signup
    path('login-signup', views.signup_login, name='signup_login'),
    # User login
    path('login', views.login_func, name='login_func'),
    # User logout
    path('logout_func', views.logout_func, name='logout_func'),
    # Product details
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    # Sending activation email
    path('email/confirmation/<str:activation_key>/', views.email_confirm, name='email_activation'),
]
