from django.urls import path
from . import views


urlpatterns = [
    path('home-instructor', views.home_instructor, name='home_instructor'),
    
]