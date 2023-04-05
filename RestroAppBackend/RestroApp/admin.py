from django.contrib import admin
from .models import RestaurantMenu, User, Order, OrderItem

# =======================================================
# Controls the fields to display in admin panel
# =======================================================

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'user_id', 
                    'user_name',
                    'user_mobile',
                    'user_email',
                    'user_address',
                    'user_role',
                    'user_password'
                    )
admin.site.register(User, UserAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'order_id', 
                    'rest_id',
                    'user_id',
                    'order_date',
                    'order_amount',
                    'order_taxes',
                    'order_net_amount',
                    'order_status',
                    'payment_mode',
                    'payment_date',
                    'payment_ref'
                    )
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'item_id', 
                    'order_id',
                    'item_quantity',                    
                    'item_price'
                    )
admin.site.register(OrderItem, OrderItemAdmin)


class RestaurantMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'item_id', 
                    'rest_id',
                    'item_name',
                    'item_type',
                    'item_price'
                    )
admin.site.register(RestaurantMenu, RestaurantMenuAdmin)

                                              

