from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm

def congrats(request):
    return HttpResponse("Congratulations! You're signed in.")

def get_name(request):
    form = NameForm()
    context = {'form':form}
    return render(request,"login/login.html",context)


