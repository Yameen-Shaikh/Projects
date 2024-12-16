from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/update/<int:pk>', UpdateDeleteProduct.as_view()),
    path('product/delete/<int:pk>', UpdateDeleteProduct.as_view()),
    path('addcart/<int:product_id>', AddCartView.as_view()),
    path('cart_details/', CartDetailView.as_view()),
    path('clear_cart/', ClearCartView.as_view()),
]