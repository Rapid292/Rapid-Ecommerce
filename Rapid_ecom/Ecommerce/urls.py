from django.urls import path
from .views import HomeView, about, ItemDetailView, checkout_page, add_to_cart


urlpatterns = [
    path("", HomeView.as_view(), name="ecom-home"),
    path("about/", about, name="ecom-about"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product-page"),
    path("add_to_cart/<slug>/", add_to_cart, name="add_to_cart"),
    path("checkout/", checkout_page, name="checkout-page"),
]
