
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login-signup', views.signup_login, name='signup_login'), # user signup
    path('login', views.login_func, name='login_func'), # user login
    path('logout_func', views.logout_func, name='logout_func'), # user logout
    # activation email
    path('email/confirmation/<str:activation_key>/', views.email_confirm, name='email_activation' ), #sending activation email
]
