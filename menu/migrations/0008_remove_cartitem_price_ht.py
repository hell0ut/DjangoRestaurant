# Generated by Django 3.1.1 on 2020-09-08 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='price_ht',
        ),
    ]
