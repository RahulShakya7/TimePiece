from urllib.parse import urlparse
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('category/', views.category, name="category"),
    path('navbar/', views.navbar, name="navbar"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)