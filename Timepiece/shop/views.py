from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'shop/home.html', context)

def category(request):
    context = {}
    return render(request, 'shop/category.html', context)

def login(request):
    context = {}
    return render(request, 'shop/InandOut.html', context)

def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)