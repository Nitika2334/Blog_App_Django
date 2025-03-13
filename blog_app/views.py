from django.shortcuts import render
#for request and response 
from django.http import HttpResponse

def blog(request):
    return HttpResponse(<h1>Hello blog app</h1>)


# Create your views here.
