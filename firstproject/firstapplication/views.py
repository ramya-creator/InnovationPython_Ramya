from django.shortcuts import render
from .models import First


from django.http import HttpResponse

def hello(request):
    #return HttpResponse("Hello World!")
    return render(request,'first.html')

