from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    # dunder
    def __str__(self):
        return f'{self.color} {self.name}'

    def get_absolute_url(self):
        return reverse("food_detail", kwargs={"pk": self.pk})
    # we use class based views here thats the onky reasib why pk was used


class Coral (models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
# heree is a many to many relationship
    food = models.ManyToManyField(Food)
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
    # this is similar to embeded relationships
    # this cat right ehre is going to directly reference the one we have above ^^
# dunder method below

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

# feeding needs to be connected to cats. so wht does the feeding need?

# we need a forign key that links the feeding to the model

# below changes the ordering


class meta:
    ordering = ('-date',)
