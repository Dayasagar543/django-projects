from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("This is the about page.")

def contactus(request):
    return HttpResponse("This is the contact us page.")

def careers(request):
    return HttpResponse("This is the careers page.")