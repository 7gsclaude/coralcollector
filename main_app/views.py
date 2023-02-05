from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Coral, Food, Feeding
from .forms import FeedingForm

# # Define the home view
# def home(request):
#     return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟﾉ</h1>')

def home (request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')


# Add new view
def coral_index(request):
    corals = Coral.objects.all
    return render(request, 'coral/index.html', { 'corals': corals })

def coral_detail(request, coral_id):
    corals = Coral.objects.get(id=coral_id)
    feeding_form = FeedingForm()
    food_not_tried = Food.objects.exclude(id__in=corals.food.all().values_list('id'))
    return render(request, 'coral/detail.html',{
        'coral':corals,
        'feeding_form': feeding_form,
        'food': food_not_tried
    })
    
    
    
    

#todoo createing a coral landing sppot adn and trying to fix this error markdown is placed where it needs to be. should be bplaced 