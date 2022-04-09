from ast import Delete
from contextlib import redirect_stderr
from django.shortcuts import render, redirect
# from .models import Details

def fnhome(request):
    if request.method=='POST':
        fname=request.POST['name']
        fphone=request.POST['phone']
        femail=request.POST['email']
        fpass=request.POST['password']
        # data=Details(name=fname,phone=fphone,email=femail,password=fpass)
        # data.save()
        return render(request,'reg.html',{'status':'successfully registered'})
    else:
        return render(request,'reg.html')
