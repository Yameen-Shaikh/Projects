from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import logging
logger = logging.getLogger(__name__)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class UpdateDeleteProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return Response({"message":"Product deleted successfully 😀"})
    


class AddCartView(APIView):
    def post(self, request, product_id):
        cart = request.session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        
        # Save the updated cart in the session
        request.session['cart'] = cart
        request.session.modified = True
        
        return Response({"message": "Product added successfully!", "cart": cart})

class CartDetailView(APIView):
    def get(self, request):
        cart = request.session.get('cart', {})  # Retrieve cart from session
        if not cart:
            return Response({"Add products to view🤌"}, status=200)

        cart_details = []
        total = 0

        # Iterate through cart items and build response data
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=int(product_id))
            cart_details.append({
                'product_id': product.id,
                'name': product.name,
                'price': float(product.price),
                'quantity': quantity,
                'total_price': float(product.price) * quantity
            })
            total += float(product.price) * quantity

        return Response({"cart": cart_details, "total": total})

class ClearCartView(APIView):
    def delete(self, request):
        request.session['cart'] = {}
        request.session.modified = True
        return Response({"message": "Cart cleared successfully!"})
