def decorator(fun):
    def greeting(*args,**kwargs):
        print('please enter your details')
        fun(*args,**kwargs)
        print('thank you for sharing your details')
    return greeting

@decorator
def register():
    name= input('enter your name ')        
    age=input('enter your age ')
register()    


    