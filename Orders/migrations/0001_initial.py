# Generated by Django 4.1.7 on 2023-04-04 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('frame_namber', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('hex_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rate', models.FloatField(default=0.5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(blank=True, max_length=255, null=True)),
                ('watsapp', models.CharField(blank=True, max_length=255, null=True)),
                ('discount', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('total_price', models.FloatField(default=0.0, verbose_name='Итоговая цена')),
                ('status', models.CharField(choices=[('DI', 'Диагностика'), ('QU', 'В очереди'), ('PR', 'В работе'), ('CO', 'Завершено')], default='DI', max_length=2)),
                ('comment', models.TextField(blank=True, null=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.bike')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.staff')),
                ('services', models.ManyToManyField(through='Orders.Operations', to='Orders.services')),
            ],
        ),
        migrations.AddField(
            model_name='operations',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order'),
        ),
        migrations.AddField(
            model_name='operations',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.services'),
        ),
        migrations.AddField(
            model_name='bike',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.color'),
        ),
        migrations.AddField(
            model_name='bike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
