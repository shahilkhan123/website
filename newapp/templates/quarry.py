from unicodedata import category


pro2=Product(title='shoe',pid='2',desp='goood',img='',price=50000,quantity=3,weight=900,weightunit='4g',category='puma',subcategory='sports',vendor='good')
pro3=Product(title='shoe',pid='3',desp='goood',img='',price=250000,quantity=3,weight=900,weightunit='4g',category='nike',subcategory='casual',vendor='bad')
pro4=Product(title='footware',pid='4',desp='very use full',img='',price=8000,quantity=2,weight=700,weightunit='3g',category='adi',subcategory='formal',vendor='usefull')
pro5=Product(title='shirt',pid='1',desp='Liked and cheap',img='',price=900,quantity=1,weight=20,weightunit='2g',category='LP',subcategory='T-shirt',vendor='half')
pro6=Product(title='pant',pid='5',desp='comfortable',img='',price=1900,quantity=1,weight=20,weightunit='2g',category='levis',subcategory='cargos',vendor='nice')


from PIL import Image
image = Image.open("reg.jpeg")