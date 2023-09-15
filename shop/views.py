from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView

from shop.models import Products, Cart


def product_view(request):
    data = Products.objects.all()
    return render(request, 'index.html', {'products': data})


@login_required
def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)

    if product.stock > 0:
        product.stock -= 1
        product.save()

    cart_item, created = Cart.objects.get_or_create(user=request.user, product_id=product_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('shop:cart_list')


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


class CartListView(ListView):
    model = Cart
    template_name = 'product/cart_list.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        # Retrieve the user's cart items
        return Cart.objects.filter(user=self.request.user)


class RemoveFromCartView(DeleteView):
    model = Cart
    template_name = 'product/cart_confirm_delete.html'  # Create this template for confirmation
    context_object_name = 'cart_item'
    success_url = reverse_lazy('shop:cart_list')

