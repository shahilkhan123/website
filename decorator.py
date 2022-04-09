from django.shortcuts import  redirect

def user_login_required(fun):
    def wrap(request,*args,**kwargs):
        if not (request.session.get('userid')):
            return redirect('/newapp/login')
        else:
            return fun(request,*args,**kwargs)    
    return wrap        