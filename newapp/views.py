from ast import Delete
from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from decorator import user_login_required
from .models import Details
# Create your views here.
def fnhome(request):
    if request.method=='POST':
        fname=request.POST['name']
        fphone=request.POST['phone']
        femail=request.POST['email']
        fpass=request.POST['password']
        data=Details(name=fname,phone=fphone,email=femail,password=fpass)
        data.save()
        return render(request,'reg.html',{'status':'successfully registered'})
    else:
        return render(request,'reg.html')


def fnemea(request):        
    return render(request,'emea.html')


def fnlogin(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        try:
            data=Details.objects.get(email=user,password=password)
            request.session['userid']=data.id
            return redirect('create')
        except Details.DoesNotExist:
            return render(request,'login.html',{'message':'Invalid user Details'})
    return render(request,'login.html')

@user_login_required
def fncreate(request):
    if request.method=='POST':
        changename=request.POST['changename']
        changephone=request.POST['changephone']
        id=request.session['userid']
        updatedel=Details.objects.filter(id=id).update(name=changename,phone=changephone)
        return redirect('create')
    else:
        id=request.session['userid']
        view=Details.objects.get(id=id)
        # del request.session['userid']
        return render(request,'create.html',{'userDetails':view})
    
def fndel(request):
    id=request.session['userid']
    Dele=Details.objects.filter(id=id).delete()
    return redirect('home')

def display(request):
    display=Details.objects.all()
    return render(request,'displaydetails.html',{'userDetails':display})


def logout(request):
    del request.session['userid']
    return redirect('login')



def fnforgot(request):
    return render(request,'forgotten.html')
def fnproduct(request):
    return render(request,'product.html') 
def fnbaabtra(request):
    return render(request,'baabtra.html')  
def fncourse(request):
    return render(request,'course.html')      
def fncontact(request):
    return render(request,'contact.html')    
def fnboot(request):
    return render(request,'bootstrap.html')    
def fnmaster(request):
    return render(request,'master.html') 
def fnindex(request):
    return render(request,'index.html')
def fncontus(request):
    return render(request,'contatus.html')    
def fnabout(request):
    return render(request,'about.html') 
def fnjava(request):
    return render(request,'java.html') 
def fncp(request):
    return render(request,'cp.html')   
def fncal(request):
    return render(request,'calculator.html')   
def fndjango(request):
    request.session['customerid']=1
    del request.session['customerid']
    company={'companyregid':100,'companyname':'baabtra','country':'india','status':'good'}
    return render(request,'django.html', {"resellerdata":company}) 
def fnnew(request):
    username=[{
        'uname':'sree',
        'place':'mongam',
        'age':23,
    },
    {
        'uname':'harshin',
        'place':'kondotty',
        'age':21,
    },
    {
         'uname':'vivek',
         'place':'Nh colony',
         'age':20,
    } ]
    return render(request,'new.html',{'responce':username}) 
    # return render(request,'new.html',{'username':'shahil'}) 
def fnform(request):
    if request.method=="POST":
        name=request.POST['username']
        passw=request.POST['password']
        if(name == "shahil " and passw == '123'):
            return render(request,'create.html') 
        else:
            return render(request,"form.html",{"ErrorMsg":"Login Failled"})
    return render(request,"form.html")
  