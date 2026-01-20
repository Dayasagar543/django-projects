from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("hi there !")
    return render(request,"home.html")


def service1(request):
    return render(request,"service1.html")

def product_page(request,product_id):
    # return HttpResponse(product_id)
    return render(request,"product_page.html",{"product_id":product_id})