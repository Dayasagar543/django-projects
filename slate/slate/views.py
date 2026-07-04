from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("Hello, World!")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def careers(request):
    return render(request, 'careers.html')