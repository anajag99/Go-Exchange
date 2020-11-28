from django.shortcuts import render
from django.http import HttpResponse
from .models import login

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html',{})

def SignUp(request):
    context = {}
    if request.method=='POST':
        data=request.POST
        r=login(fname=data["first_name"], lname=data["last_name"], email_id=data["email_id"],country=data["country"],state=data["state"],city=data["city"], password=data["password"],confirmpassword=["confirmpassword"])
        r.save()
        context = {'display':"Registered Successfully"}

    return render(request,"GoExchange.html",context)
    
def GoExchange(request):
    return render(request,'GoExchange.html',{})

def section2(request):
    return redirect(request,'dashboard.html',{})

def compared(request):
    return render(request,'compared.html',{})