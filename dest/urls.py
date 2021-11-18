from django.contrib import admin
from django.urls import path
from dest import views
urlpatterns = [
    path('', views.dest, name='dest'),
    path('hotels/', views.hotels, name='hotels'),     
    path('bookmark/', views.bookmark, name='bookmark'),    
    path('<str:slug>/', views.detail, name='detail'),
]
