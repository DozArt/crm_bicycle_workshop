from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import OrderForm, OrderUpdateForm, BikeForm
from .models import Order, Bike


class Chapter:
    pass


class OrdersList(ListView):
    model = Order
    ordering = '-time_in'
    template_name = 'orders.html'
    context_object_name = 'orders'
    paginate_by = 2


class OrderDetail(DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'


class OrderCreate(CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'order_create.html'


class OrderUpdate(UpdateView):
    form_class = OrderUpdateForm
    model = Order
    template_name = 'order_update.html'


class BikeList(ListView):
    model = Bike
    ordering = 'model'
    template_name = 'bikes.html'
    context_object_name = 'bikes'
    paginate_by = 2


class BikeDetail(DetailView):
    model = Bike
    template_name = 'bike.html'
    context_object_name = 'bike'


class BikeCreate(CreateView):
    form_class = BikeForm
    model = Bike
    template_name = 'bike_create.html'
