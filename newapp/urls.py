from django.urls import path
from . import views

urlpatterns=[
    path('home', views.fnhome, name='home'),
    path('emea/', views.fnemea, name='emea'),
    path('fb', views.fnfb, name='fb'),
    path('create', views.fncreate, name='create'),
    path('forgot', views.fnforgot, name='forgot'),
    path('product',views.fnproduct,name='product'),
    path('baabtra',views.fnbaabtra,name='baabtra'),
    path('course',views.fncourse,name='course'),
    path('contact',views.fncontact,name='contact'),
    path('boot',views.fnboot,name='boot'),
    path('master',views.fnmaster,name='master'),
    path('index',views.fnindex,name='index'),
    path('contus',views.fncontus,name='contact us'),
    path('about',views.fnabout,name='about'),
    path('java',views.fnjava,name='java'),
    path('cp',views.fncp,name='cp'),
   




    
]