from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import userform

def home(request):
    # return HttpResponse("Hello, world. You're at the jgs index.")
    return render(request, 'base.html')

def about(request):
    
    return render(request, 'about.html')

def contactus(request):
    
    return render(request, 'contactus.html')

def service1(request):
    
    return render(request, 'service1.html')


def thankyou(request):
    return render(request, 'thankyou.html')

def form(request):
    sum_value=0
    try:
        if request.method=="GET":
            num1=int(request.GET['first_value']) 
            num2=int(request.GET['second_value'])
            sum_value=num1+num2
    except:
        pass
    return render(request, 'form.html',{'result':sum_value})


def form2(request):
    sum_value=0
    try:
        if request.method=="POST":
            num1=int(request.POST['first_value']) 
            num2=int(request.POST['second_value'])
            sum_value=num1+num2
            return redirect('/thankyou/')
    except:
        pass
    
    return render(request, 'form2.html',{'result':sum_value})

def user_form(request):
    data={}
    if request.method=="POST":
        form=userform()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(name,email,message)
        data['Name']=name
        data['Email']=email 
        data['Message']=message
    
        return render(request, 'thankyou.html',data)
    else:
        form=userform()
    return render(request, 'userform.html',{'form':form})
