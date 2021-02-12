from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import NameForm


def sign_up(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')


    else:
        form = NameForm()
        context = {'form':form}
    return render(request,"signup/signup.html",context)






