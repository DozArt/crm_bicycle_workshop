from django.urls import path
from .views import OrdersList, OrderDetail, OrderCreate

urlpatterns = [
   path('', OrdersList.as_view()),
   path('<int:pk>', OrderDetail.as_view()),
   path('create/', OrderCreate.as_view(), name='order_create'),
]
