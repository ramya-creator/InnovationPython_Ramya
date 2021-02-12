from django.shortcuts import render,get_object_or_404,redirect
from .models import newblog
from .forms import NameForm
from django.contrib.auth.models import User,auth
from django.contrib import messages

def blog_list(request):
    fields = newblog.objects.all()
    context = {'fields':fields}
    return render(request,"blog/home.html", context)

def aboutUs(request):
    return render(request,"blog/aboutUs.html")

def create(request):
    form = NameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,"blog/home.html")
    else:
        form = NameForm()
        context = {"form":form}
    return render(request, "blog/post_form.html",context)

def blog_delete(request,pk):
    data = get_object_or_404(newblog,pk=pk)
    if request.method == "POST":
        data.delete()
        return render(request,"blog/home.html")
    return render(request,"blog/post_delete.html")

def home(request):
    return render(request,"home.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def test(request):
    return render(request,"blog/home.html")

