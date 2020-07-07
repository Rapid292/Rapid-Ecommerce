from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order


def about(request):
    context = {"items": Item.objects.all()}
    return render(request, "about.html", context)


class HomeView(ListView):
    model = Item
    template_name = "home-page.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"


def checkout_page(request):
    context = {"items": Item.objects.all()}
    return render(request, "checkout-page.html", context)


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order
        if order_item.filter(item_slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
    return redirect("product-page", kwargs={"slug": slug})

