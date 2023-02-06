from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Coral, Meds, Feeding
from .forms import FeedingForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

#this detail function got updated at the very end in order to show the relationships between the medication  

def coral_detail(request, coral_id):
    corals = Coral.objects.get(id=coral_id)
    feeding_form = FeedingForm()
    meds_not_tried = Meds.objects.exclude(id__in=corals.meds.all().values_list('id'))
    return render(request, 'coral/detail.html',{
        'coral':corals,
        'feeding_form': feeding_form,
        'med': meds_not_tried
#above is returning each model into this function  

        # feeding_formis set to an instance of FeedingFormand then it's passed to detail.html just like coral.
    })
    
def add_feeding(request, coral_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit = False)
        new_feeding.coral_id = coral_id
        new_feeding.save()
    return redirect('detail', coral_id=coral_id)
    
    # for there to be a relationship between certain things,this must be established 
def assoc_med(request, coral_id,med_id):
  Coral.obejcts.get(id=coral_id).med.add(med_id)
  return redirect('detail', cat_id=med_id)
    
    
class CoralCreate(CreateView):
    model = Coral 
    fields = '__all__'
    success_url = '/corals/'

   # this form takes the self anf form
#    renders a form with the users instance from the selfs user request
### this function is for the user auth i believe  
#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        #to hand this back to wehere its pulled you involk super
#        return super().form_valid(form)
       
       

class CoralUpdate(UpdateView):
  model = Coral
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'description', 'species', 'price']

class CoralDelete(DeleteView):
  model = Coral
  success_url = '/corals/'
    
    

#todoo createing a coral landing sppot adn and trying to fix this error markdown is placed where it needs to be. should be bplaced 


class MedsIndex(LoginRequiredMixin, ListView):
  model = Meds


class MedsCreate (LoginRequiredMixin, CreateView):
  model = Meds
  fields = '__all__'


class MedsDetail(LoginRequiredMixin, DetailView):
  model = Meds


class MedsDelete(LoginRequiredMixin, DeleteView):
  model = Meds
  success_url = '/meds/'


class MedsUpdate(LoginRequiredMixin, UpdateView):
  model = Meds
  fields = '__all__'
