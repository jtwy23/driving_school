from django.shortcuts import render

# Create your views here.

def my_orders(request):
    return render(request, 'my_order.html')


# cart page
def cart(request):
    return render(request, 'shoping-cart.html')
