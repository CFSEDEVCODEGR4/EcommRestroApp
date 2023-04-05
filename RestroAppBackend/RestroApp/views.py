from rest_framework import generics
from RestroApp.serializers import  RestaurantMenuSerializer, UserSerializer, OrderSerializer,OrderItemSerializer
from RestroApp.serializers import  RestaurantMenu, User, Order,OrderItem
               

# ===================================================
# User
# ===================================================
class USerList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = User.objects.all()
        # Allow filter/search using mobile as query parameter
        in_user_id = self.request.query_params.get('user_id', None)
        if (in_user_id is not None):
            queryset = queryset.filter(user_id = in_user_id)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# ===================================================
# Order
# ===================================================
class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = Order.objects.all()
        # Allow filter/search using mobile as query parameter
        in_order_id = self.request.query_params.get('order_id', None)
        if (in_order_id is not None):
            queryset = queryset.filter(order_id = in_order_id)
        return queryset

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


# ===================================================
# OrderItem
# ===================================================
class OrderItemList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def get_queryset(self):
        queryset = OrderItem.objects.all()
        # Allow filter/search using mobile as query parameter
        in_item_id = self.request.query_params.get('item_id', None)
        if (in_item_id is not None):
            queryset = queryset.filter(item_id = in_item_id)
        return queryset

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all() 

# ===================================================
# RestaurantMenu
# ===================================================
class RestaurantMenuList(generics.ListCreateAPIView):
    serializer_class = RestaurantMenuSerializer
    queryset = RestaurantMenu.objects.all()

    def get_queryset(self):
        queryset = RestaurantMenu.objects.all()
        # Allow filter/search using mobile as query parameter
        in_item_id = self.request.query_params.get('item_id', None)
        if (in_item_id is not None):
            queryset = queryset.filter(item_id = in_item_id)
        return queryset

class RestaurantMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantMenuSerializer
    queryset = RestaurantMenu.objects.all()    
        








