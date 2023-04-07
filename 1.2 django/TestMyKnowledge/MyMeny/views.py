from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Index part start
def index(request):
    return render(request, "main/index.html")
# Index part end


# FAQ Part start
def FAQ (request):
    return render(request, "FAQ/FAQ.html")

def author(request):
    return render(request, "FAQ/author/author.html")