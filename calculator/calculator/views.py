from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms

def home(request):
    return render(request, 'base.html')


def calculator_view(request):
    num1=0
    num2=0
    result=0
    if request.method =='POST':
        value1=request.POST.get('num1')
        value2=request.POST.get('num2')
        operation=request.POST.get('operation')
        num1=int(value1)  
        num2=int(value2)
        if operation=='+':
            result=num1+num2
        elif operation=='-':
            result=num1-num2
        elif operation=='*':
            result=num1*num2
        elif operation=='/':
            result=num1/num2
        
   
    return render(request, 'calculator.html',{'num1':num1,'num2':num2,'result':result})

def even_odd(request):
  result=0
  try:
      if request.method=='POST':
          value=request.POST.get('num')
          num=int(value)
          if num%2==0:
              result="The number is Even"
          else:
              result="The number is Odd"
  except ValueError:
      result="Please enter a valid integer"
  return render(request, 'even_odd.html',{'result':result})

        
def advanced_cal(request):

    # using get
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operation = request.GET.get('operation')
    result = None

    if num1 is not None and num2 is not None and operation:
        try:
            num1 = int(num1)
            num2 = int(num2)

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

        except ValueError:
            result = "Please enter valid numbers"

    return render(request, "advanced_calculator.html", {
        "num1": num1,
        "num2": num2,
        "result": result
    })
