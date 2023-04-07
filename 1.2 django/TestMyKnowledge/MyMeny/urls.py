from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.FAQ, name = "FAQ"),
    path("author/", views.author, name="author"),
]