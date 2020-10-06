from django.views.generic import ListView,DetailView
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


class FoodDetail(DetailView):
    model = Food


class AllFood(ListView):
    model = Food

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.datetime.now().strftime("%H:%M:%S")
        context['object_list']=Food.objects.filter(category=self.kwargs.get('pk'))
        return context

def hotel_image_view(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('menu:main')
    else:
        form = FoodForm()
    return render(request, 'menu/food_form.html', {'form': form})


class CategoryView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.datetime.now().strftime("%H:%M:%S")
        return context


