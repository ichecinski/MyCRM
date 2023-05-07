from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead-list'),
    path('<int:pk>/', views.lead_detail, name='lead-detail'),
    path('<int:pk>/update/', views.lead_update, name='lead-update'),
    path('create/', views.lead_create, name='lead-create'),

]
