# Generated by Django 4.1.7 on 2023-04-05 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='Rate',
            new_name='rate',
        ),
    ]