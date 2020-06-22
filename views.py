"""
from django.http import HttpResponse

def index(request):
     return HttpResponse("Hello,Paphu")
"""
from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html', {})

def demo(request):
    return render(request, 'app/demo.html', {})
def dealer(request):
    return render(request, 'app/dealer.html', {})
def cliente(request):
    return render(request, 'app/cliente.html', {})
def calendar(request):
    return render(request, 'app/calendar.html', {})