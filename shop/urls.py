from django.urls import path
from .views import product_view, ProductDetailView, CartListView, add_to_cart, RemoveFromCartView

app_name = 'shop'

urlpatterns = [
    path('', product_view, name='product_list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', CartListView.as_view(), name='cart_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]