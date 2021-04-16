
from django.urls import path
from . import views
from .views import PaymentView

urlpatterns = [
    path('my_orders', views.my_orders, name='my_orders'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', PaymentView.as_view(), name='payment'),
    
]
