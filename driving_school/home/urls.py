
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_lessons', views.all_lessons, name='all_lessons'),  # All lessons
    path('product_search', views.product_search, name='product_search'),  # Searching for products
    path('profile', views.profile, name='profile'),  # User profile
    path('edit_profile', views.edit_profile, name='edit_profile'),  # User profile edit
    path('login-signup', views.signup_login, name='signup_login'),  # User signup
    path('login', views.login_func, name='login_func'),  # User login
    path('logout_func', views.logout_func, name='logout_func'),  # User logout
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),  # Product details
    path('email/confirmation/<str:activation_key>/', views.email_confirm, name='email_activation' ),  # Sending activation email
]
