from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Services(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name}'


class Staff(models.Model):  # Работник
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.FloatField(default=0.5)

    def __str__(self):
        return f'{self.user}'


class Color(models.Model):
    name = models.CharField(max_length=64)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.name}'


class Bike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    frame_namber = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.model} - {self.color}'


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

    executor = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Испольнитель', null=True, blank=True)  # Исполнитель
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    services = models.ManyToManyField(Services, through='Operations', verbose_name='Услуги')

    def __str__(self):
        return f'{self.bike} - {self.comment}'

    def get_absolute_url(self):
        return reverse('order_update', args=[str(self.id)])


class Operations(models.Model):  # ServicesOrder
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


class Profile(models.Model):  # добавить телефон
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    watsapp = models.CharField(max_length=255, null=True, blank=True)
    discount = models.FloatField(default=0.0)
