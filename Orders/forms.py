from django import forms
from .models import Order, Bike


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'bike',
            'comment',
        ]


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'bike',
            'comment',
            'services',
        ]


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = [
            'model',
            'color',
            'user',
            'frame_namber',
        ]
