from django.shortcuts import render
from django.http import HttpResponse
def app2_string(request):
    return HttpResponse('<h1><marquee>this is app2_string</marquee></h1>')

    
def app2(request):
    return render(request,'app2.html')

# Create your views here.
