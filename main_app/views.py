from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse

from .models import Coral, Food

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

#todoo createing a coral landing sppot adn and trying to fix this error markdown is placed where it needs to be. should be bplaced 