from django.shortcuts import render

# Create your views here.
def fnhome(request):
    return render(request,'index.html')