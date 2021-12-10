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