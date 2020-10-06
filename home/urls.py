from .views import Home
from django.urls import path,include

app_name = 'home'


urlpatterns = [
    path('',Home.as_view(),name='main'),
]