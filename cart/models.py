from django.db import models
from menu.models import *
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    quanity = models.PositiveIntegerField()
    cart=models.ForeignKey('Cart',on_delete=models.CASCADE)