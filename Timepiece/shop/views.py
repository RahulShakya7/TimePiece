from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import *
import json
import datetime

# Create your views here.
def loginuser(request):
    if request.method == "POST":
        user = authenticate(request, 
        username=request.POST['username'], 
        password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'shop/home.html')
        else:
            return render(request, 'shop/login.html')
    else:
        return render(request, 'shop/login.html')

@login_required(login_url='shop/loginuser')
def logout(request):
    logout(request)
    return redirect('/')

def register(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        User.objects.create_user(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
        print(request.POST)
        return redirect('loginuser')
    else:
        return render(request, 'shop/register.html')

# @login_required(login_url='shop/loginuser')
def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order}

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'shop/home.html', context)

# @login_required(login_url='shop/loginuser')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}

    return render(request, 'shop/cart.html', context)

# @login_required(login_url='shop/loginuser')
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was Added', safe=False)

# @login_required(login_url='shop/loginuser')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}

    return render(request, 'shop/checkout.html', context)

# @login_required(login_url='shop/loginuser')
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create (
                customer=customer,
                order=order,
                city=data['shipping']['city'],
                address=data['shipping']['address'],
                zipcode=data['shipping']['zipcode'],
            )

    return JsonResponse('Payment completed', safe=False)