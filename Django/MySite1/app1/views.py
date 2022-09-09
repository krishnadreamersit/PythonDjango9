from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    str1 = """
    <html>
        <head>
            <title>first page</title>
        </head>
        <body>
            <h1>Welcome to django</h1>
        </body>
    </html>
    """
    return HttpResponse(str1)

def about(request):
    return HttpResponse("Hello from about")
def services(request):
    return HttpResponse("Hello from services")
def contact(request):
    return HttpResponse("Hello from contact")