from .views import *
from django.urls import path


app_name = 'menu'

urlpatterns = [
    path('',CategoryView.as_view(), name='main'),
    path('add_food', hotel_image_view, name='add_food'),
    path('<int:pk>',AllFood.as_view(),name='food_list'),
    path('<int:pk>/<int:id>',FoodDetail.as_view(),name='food_detail'),
]