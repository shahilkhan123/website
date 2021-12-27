from django.shortcuts import render

# Create your views here.
def fnhome(request):
    return render(request,'reg.html')

def fnemea(request):
    return render(request,'emea.html')
def fnfb(request):
    return render(request,'fb.html')
def fncreate(request):
    return render(request,'create.html')
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
