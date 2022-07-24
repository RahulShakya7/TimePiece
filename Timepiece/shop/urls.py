from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('category/', views.category, name="category"),
    path('login', views.login, name="login"),
    path('update_item/', views.updateItem, name="update"),
] 