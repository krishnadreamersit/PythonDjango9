import http.client

from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def home(request):
    return render(request, 'app2/index.html')

def showForm(request):
    return render(request, 'app2/form1.html')

def getForm(request):
    # receive
    if(request.method=='GET'):
        num1 = int(request.GET.get('txtNum1'))
        num2 = int(request.GET.get('txtNum2'))
    if request.method=='POST':
        num1 = int(request.POST.get('txtNum1'))
        num2 = int(request.POST.get('txtNum2'))

    # calculate
    num3 = num1 + num2
    # display
    str1 = "<h1>Calculation</h1>"
    str1 +="<p>NUM1 : {}".format(num1)
    str1 +="<p>NUM2 : {}".format(num2)
    str1 +="<p>RESULT : {}".format(num3)
    return HttpResponse(str1)