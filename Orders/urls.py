from django.urls import path
from .views import OrdersList, OrderDetail, OrderCreate, OrderUpdate, BikeList, BikeDetail, BikeCreate

urlpatterns = [
   path('orders/', OrdersList.as_view(), name='order_list'),
   path('orders/<int:pk>', OrderDetail.as_view(), name='order_detail'),
   path('orders/create/', OrderCreate.as_view(), name='order_create'),
   path('orders/<int:pk>/update', OrderUpdate.as_view(), name='order_update'),
   path('bikes/', BikeList.as_view(), kwargs={"chapter": "order"}, name='bike_list'),
   path('bikes/<int:pk>', BikeDetail.as_view(), name='bike_detail'),
   path('bikes/create/', BikeCreate.as_view(), name='bike_create'),
]
