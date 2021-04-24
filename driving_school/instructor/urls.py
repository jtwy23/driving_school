from django.urls import path
from . import views


urlpatterns = [
    path('home-instructor', views.home_instructor, name='home_instructor'),  # Instructor home
    path('login-instructor', views.login_func_instructor, name='login_func_instructor'),  # Instructor login
    path('my_lessons', views.my_lessons, name='my_lessons'),  # Instructor lessons 
    path('instructor_profile', views.instructor_profile, name='instructor_profile'),  # Instructor profile
    path('order_details/<int:pk>', views.order_details, name='order_details'),  # Instructor order detail
    path('cancel_order', views.make_cancel_order, name='make_cancel_order'),  # Instructor cancel
    path('make_complete_order', views.make_complete_order, name='make_complete_order')#complete the order
]