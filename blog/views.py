from django.shortcuts import render
from django.hhtp import HttpResponse

def home(request):
    return HttpResponse('<h1>blog home</h1>')
