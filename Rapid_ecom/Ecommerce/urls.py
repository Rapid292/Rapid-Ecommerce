from django.urls import path
from .views import (
    HomeView,
    about,
    ItemDetailView,
    checkout_page,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
)


urlpatterns = [
    path("", HomeView.as_view(), name="ecom-home"),
    path("about/", about, name="ecom-about"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product-page"),
    path("order_summary/", OrderSummaryView.as_view(), name="order_summary"),
    path("add_to_cart/<slug>/", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<slug>/", remove_from_cart, name="remove_from_cart"),
    path(
        "remove_single_item_from_cart/<slug>/",
        remove_single_item_from_cart,
        name="remove_single_item_from_cart",
    ),
    path("checkout/", checkout_page, name="checkout-page"),
]
