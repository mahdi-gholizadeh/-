from django.contrib import admin
from django.urls import path



appname='sabad'
urlpatterns = [




]



from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:detail_id>/', views.remove_from_cart, name='remove_from_cart'),
]











