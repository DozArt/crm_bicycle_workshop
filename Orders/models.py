from django.contrib.auth.models import User
from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):  # Работник
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Rate = models.FloatField(default=0.5)


class Color(models.Model):
    name = models.CharField(max_length=64)
    hex_code = models.CharField(max_length=7)


class Bike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    frame_namber = models.CharField(max_length=255, null=True, blank=True)


class Order(models.Model):  # Заказ
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)  # пустая если еще не готов
    total_price = models.FloatField(default=0.0, verbose_name='Итоговая цена')

    diagnostics = 'DI'
    queue = 'QU'
    processed = 'PR'
    completed = 'CO'

    STATUS = [
        (diagnostics, 'Диагностика'),
        (queue, 'В очереди'),
        (processed, 'В работе'),
        (completed, 'Завершено'),
    ]

    status = models.CharField(max_length=2,  # Добавить метод - если статус завершен
                              choices=STATUS,
                              default=diagnostics)

    executor = models.ForeignKey(Staff, on_delete=models.CASCADE)  # Исполнитель
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)

    services = models.ManyToManyField(Services, through='Operations')


class Operations(models.Model):  # ServicesOrder
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    watsapp = models.CharField(max_length=255, null=True, blank=True)
    discount = models.FloatField(default=0.0)
