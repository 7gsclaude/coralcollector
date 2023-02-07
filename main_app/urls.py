
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
    path('corals/<int:cat_id>add_feeding/', views.add_feeding, name='add_feeding'),
    
    path('meds/', views.MedsIndex.as_view(), name='med_index'),
    path('meds/create', views.MedsCreate.as_view(), name='med_create'),
    path('meds/<int:pk>/', views.MedsDetail.as_view(), name='med_detail'),
    path('meds/<int:pk>/update', views.MedsUpdate.as_view(), name='med_update'),
    path('meds/<int:pk>/delete', views.MedsDelete.as_view(), name='med_delete'),


    # this path assoiatees meds to a specifc cat
    path('corals/<int:coral_id>/assoc_med/<int:med_id>/',views.assoc_med, name='assoc_med'),

    
    path('accounts/signup/', views.signup, name='signup')

    

]
