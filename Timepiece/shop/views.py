from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/home.html', context)

def category(request):
    context = {}
    return render(request, 'shop/category.html', context)

def login(request):
    context = {}
    return render(request, 'shop/InandOut.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}

    return render(request, 'shop/cart.html', context)

def updateItem(request):
    return JsonResponse('Item added', safe=False)
