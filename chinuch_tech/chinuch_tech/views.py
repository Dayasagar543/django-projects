from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,"home.html")


def aboutus(request):
    return render(request,"AboutUs.html")

def countactus(request):
    return render(request,"ContactUs.html")

def ourprograms(request):
    return render(request,"Our_pragrams.html")

def Carrers(request):
    return render(request,"Carrers.html")

def program_detailing_page(request):
    return render(request,"Program_detailing_page.html")

def page404(request):
    return render(request,"Program_detailing_page.html")