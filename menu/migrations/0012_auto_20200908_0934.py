# Generated by Django 3.1.1 on 2020-09-08 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_remove_cart_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quanity',
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price_ht', models.FloatField(blank=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.food')),
            ],
        ),
    ]