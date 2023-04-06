from django.views.generic import ListView, DetailView, CreateView

from .forms import OrderForm
from .models import Order


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
    template_name = 'order_edit.html'
