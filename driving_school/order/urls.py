
from django.urls import path
from . import views


urlpatterns = [
    path('my_orders', views.my_orders, name='my_orders'),
    path('cart', views.cart, name='cart'),
    
]
