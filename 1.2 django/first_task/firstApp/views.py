from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord, Topic, Webpage, UsersData
# Create your views here.


def index(request):
    return HttpResponse("Hello world!")


def firstApp(request):
    webpages_list = UsersData.objects.order_by('username')
    users_dict = {'user_data' : webpages_list}

    return render(request, 'firstApp/index.html', context = users_dict)


def author(request):
    return HttpResponse("Author of this page is Alexey Arkhipov")
