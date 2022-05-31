from django.shortcuts import render
from .models import Product,Comment
from .forms import CommentForm 

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
    comments=x.comments.all()
    comment_form=CommentForm()
    if request.method=='POST':
     comment_form= CommentForm(data=request.POST)
     print("x",x)
     if comment_form.is_valid():
         new_comment=comment_form.save(commit=False)
         new_comment.product=x
         new_comment.save() 
         comment_form=CommentForm()
    else:
        comment_form= CommentForm()
    return render(request,'products/product.html', {"pro" : x,'comments':comments,'newComment':comment_form})
def delete_product(request,id):
    x=Product.objects.get(pk=id).delete()
    return render(request,'products/products.html',{'pro':Product.objects.all()})


