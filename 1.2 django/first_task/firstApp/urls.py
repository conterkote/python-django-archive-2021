from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstApp),
    path('author/', views.author),
]
