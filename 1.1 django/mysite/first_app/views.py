from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Now I am coming from first_app/index.html'}
    return render(request, 'first_app/index.html', context=my_dict)


def help(request):
    my_dict = {'insert_me': 'Welcome to the help page!'}
    return render(request, 'first_app/help.html', context=my_dict)
