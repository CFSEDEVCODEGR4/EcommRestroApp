from django.urls import path
from RestroApp import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Swagger API docs",
      default_version='v1',
      description="Swagger API docs description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

#============================================================================
# API URL  http://127.0.0.1:8000/restroapp/api/customers
#============================================================================
urlpatterns = [         

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),                        
  
     # =============
    # User
    # =============
    path('api/user/', views.USerList.as_view()),             
    path('api/user/<int:pk>', views.UserDetail.as_view()),


     # =============
    # Order
    # =============
    path('api/order/', views.OrderList.as_view()),             
    path('api/order/<int:pk>', views.OrderDetail.as_view()),

    # =============
    # OrderItem
    # =============
    path('api/orderItem/', views.OrderItemList.as_view()),             
    path('api/orderItem/<int:pk>', views.OrderItemDetail.as_view()),


    # =============
    # RestaurantMenu
    # =============
    path('api/restaurantmenu/', views.RestaurantMenuList.as_view()),             
    path('api/restaurantmenu/<int:pk>', views.RestaurantMenuDetail.as_view())  

    
               

] 
