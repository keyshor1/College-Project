from django.contrib import admin
from . models import Cart, Customer, OrderPlaced, Payment, Product
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    # def products(self,obj):
    #     link = reverse("admin:app_product_change",args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>',link,obj.Product.title)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']

# @admin.regiser(Wishlist)
# class WishlistModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'product']