from django.urls import path
from . import views

app_name = 'cartapp'

urlpatterns = [
    path('add_cart/<int:product_id>/',views.add_cart, name= 'add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('cart_remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/',views.delete, name='delete'),


]