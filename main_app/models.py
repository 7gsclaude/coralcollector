from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.


class Meds(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    # dunder
    def __str__(self):
        return f'{self.color} {self.name}'

    def get_absolute_url(self):
        return reverse("med_detail", kwargs={"pk": self.id})
    #changed self to .id 
    # we use class based views here thats the onky reasib why pk was used


class Coral (models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
# heree is a many to many relationship
    meds = models.ManyToManyField(Meds) 
    # these feidls also correspeond with what is found in the admin login site 
    
# this str line helps print the text in a better way 
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("detail", kwargs={"coral_id": self.id})


class Feeding(models.Model):
    MEALS = (
        ('R', 'ReefRoids'),
        ('A', 'Brightwell Ab+'),
        ('B', 'Benepets'),
    )
    date = models.DateField('feeing date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    coral = models.ForeignKey(Coral, on_delete=models.CASCADE)
    #cascade means that when corals are deleted so will the model for feeding. 
    # this is similar to embeded relationships
    # this cat right ehre is going to directly reference the one we have above ^^
# dunder method below

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

# feeding needs to be connected to cats. so wht does the feeding need?

# we need a forign key that links the feeding to the model

# below changes the ordering
#here is the link to include specifications on fed corals in the future . 
# https://seir-1114.netlify.app/second-language/week-2/day-3/lecture-materials/intro-to-django-one-to-many-relationships


class meta:
    ordering = ('-date',)
