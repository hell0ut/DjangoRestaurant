from .views import *
from django.urls import path


app_name = 'info'

urlpatterns = [
    path('', Info.as_view(), name='main'),
]