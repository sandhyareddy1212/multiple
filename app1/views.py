from django.shortcuts import render
from django.http import HttpResponse
def app1_string(request):
    return HttpResponse('<h1><marquee>this is app1_string</marquee></h1>')
def app1(request):
    return render(request,'app1.html')
# Create your views here.
