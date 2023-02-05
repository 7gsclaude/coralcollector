
from django.urls import path
from . import views
from django.contrib import admin
# Add the include function to the import


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('corals/', views.coral_index, name='index'), 
    path('corals/<int:coral_id>/', views.coral_detail, name='detail'),
    path('corals/create/', views.CoralCreate.as_view(), name='corals_create'),
    path ('corals/<int:pk>/update', views.CoralUpdate.as_view(), name='corals_update'),
    path ('corals/<int:pk>/delete', views.CoralDelete.as_view(), name='corals_delete'),
    # path('cats/<int:cat_id>add_feeding/', views.add_feeding, name='add_feeding'),
]
