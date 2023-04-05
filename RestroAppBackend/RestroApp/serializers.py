from rest_framework import serializers
from RestroApp.models import RestaurantMenu, User,Order, OrderItem

# ============================================================
# User
# ============================================================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  'id',
                  'user_id', 
                  'user_name',
                  'user_mobile',
                  'user_email',
                  'user_address', 
                  'user_role',
                  'user_password'
                ]  

# ============================================================
# Order
# ============================================================
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
                  'id',
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
                ]        

# ============================================================
# OderItem Menu
# ============================================================
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
                  'id',
                  'item_id', 
                  'order_id',
                  'item_quantity',
                  'item_price'
                ]                         

# ============================================================
# Restaurant Menu
# ============================================================
class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = [
                  'id',
                  'item_id', 
                  'rest_id',
                  'item_name',
                  'item_type',
                  'item_price', 
                ]                     
