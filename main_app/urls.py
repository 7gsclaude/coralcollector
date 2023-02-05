
from django.urls import path
from . import views
from django.contrib import admin
# Add the include function to the import


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('corals/', views.coral_index, name='index'), 
    path('coral/<int:coral_id>/', views.coral_detail, name='detail'),

    # path ('corals/create/', views.CoralCreate.as_view(), name='coral_update'),
    # path ('corals/delete/', views.CoralCreate.as_view(), name='coral_delete'),

    # path('corals/', views.corals_index, name='index'),
    #below is the show route i believe
    # path('corals/<int:coral_id>/', views.coral_detail, name='detail')
]
