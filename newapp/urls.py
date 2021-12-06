from django.urls import path
from . import views

urlpatterns=[
    path('home', views.fnhome, name='home'),
    path('emea/', views.fnemea, name='emea'),
    path('fb', views.fnfb, name='fb'),
    path('create', views.fncreate, name='create'),
    path('forgot', views.fnforgot, name='forgot'),
   




    
]