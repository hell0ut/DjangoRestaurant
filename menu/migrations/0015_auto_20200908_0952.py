# Generated by Django 3.1.1 on 2020-09-08 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20200908_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
