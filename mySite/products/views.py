from django.shortcuts import render
from .models import Product
def products(requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.all()})
def book (requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='book')})
def PostersPrints (requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='PostersPrints')})
def RIDINGBOOTS (requset):
 return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='RIDINGBOOTS')})
def ChildrensRidingWear (requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='ChildrensRidingWear')})
def Helmets (requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='Helmets')})
def Gloves (requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='Gloves')})
def WomensTightsBreeches(requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='def WomensTightsBreeches(requset):')})
def BodyProtectors (requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='BodyProtectors')})
def WomensRidingClothing (requset):
    return render(requset,'products/products.html',	{'pro':Product.objects.filter(category='WomensRidingClothing')})
def product(request,id):
    x=Product.objects.get(pk=id)
    return render(request,'products/product.html', {"pro" : x})

