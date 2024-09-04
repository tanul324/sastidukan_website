from django.contrib import admin
from .models import cart,cartitem,order

# Register your models here.
@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
    

    list_display = ('id','user','created_at')
    
@admin.register(cartitem )
class cartitemAdmin(admin.ModelAdmin):


    list_display = ('product','cart','quantity','added_at')
    
    list_filter = ('added_at',)
    ordering = ('added_at',)

@admin.register(order)
class orderAdmin(admin.ModelAdmin):


    list_display = ('user','product','quantity','is_paid','is_delivered','ordered_at')
    list_filter = ('ordered_at','is_paid','is_delivered')
