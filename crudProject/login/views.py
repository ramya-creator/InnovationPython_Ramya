from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NameForm

def success(request):
    return HttpResponse("Hello")

def log_in(request):
    if request.method == 'POST':
        form = NameForm(data=request.POST)
        if form.is_valid():
            return redirect('/login/success')
    else:
        form = NameForm()
        context = {'form':form}
    return render(request,"login/login.html",context)

