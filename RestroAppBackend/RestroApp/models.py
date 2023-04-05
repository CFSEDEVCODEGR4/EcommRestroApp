from django.db import models
from django.urls import reverse

# ===============================================================
# User Model
# ===============================================================
class User(models.Model):    
    user_id = models.CharField(max_length = 10) 
    user_name = models.CharField(max_length = 40)
    user_mobile = models.CharField(max_length = 120) 
    user_email = models.CharField(max_length = 20)
    user_address = models.CharField(max_length = 20)
    user_role = models.CharField(max_length = 20)
    user_password = models.CharField(max_length = 20)
    class Meta:
        ordering = ['user_id']

    def get_absolute_url(self):
        return reverse('User-details', args=[str(self.id)])   
        
    def __str__(self):
        return self.user_id


# ===============================================================
# Order Model
# ===============================================================
class Order(models.Model):    
    order_id = models.CharField(max_length = 10) 
    rest_id = models.CharField(max_length = 40)
    user_id = models.CharField(max_length = 120) 
    order_date = models.CharField(max_length = 20)
    order_amount = models.CharField(max_length = 20)
    order_taxes = models.CharField(max_length = 20)
    order_net_amount = models.CharField(max_length = 20)
    order_status = models.CharField(max_length = 20)
    payment_mode = models.CharField(max_length = 20)
    payment_date = models.CharField(max_length = 20)
    payment_ref = models.CharField(max_length = 20)

    class Meta:
        ordering = ['order_id']

    def get_absolute_url(self):
        return reverse('Order-details', args=[str(self.id)])   
        
    def __str__(self):
        return self.order_id        


# ===============================================================
# OrderItem Model
# ===============================================================
class OrderItem(models.Model):    
    item_id = models.CharField(max_length = 10)
    order_id = models.CharField(max_length = 40)  
    item_quantity = models.CharField(max_length = 40)
    item_price = models.CharField(max_length = 120)    
    class Meta:
        ordering = ['item_id']

    def get_absolute_url(self):
        return reverse('OrderItem-details', args=[str(self.id)])   
        
    def __str__(self):
        return self.item_id

# ===============================================================
# RestaurantMenu Model
# ===============================================================
class RestaurantMenu(models.Model):    
    item_id = models.CharField(max_length = 10)
    rest_id = models.CharField(max_length = 40)  
    item_name = models.CharField(max_length = 40)
    item_type = models.CharField(max_length = 120) 
    item_price = models.CharField(max_length = 20)
    class Meta:
        ordering = ['item_id']

    def get_absolute_url(self):
        return reverse('RestaurantMenu-details', args=[str(self.id)])   
        
    def __str__(self):
        return self.item_id




