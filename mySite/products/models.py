from typing import OrderedDict
from django.db import models

class Product(models.Model):
    categoryList=[('book','Book'),('PostersPrints','Posters & Prints')
    ,('RIDINGBOOTS&CHAPS ','RIDINGBOOTS&CHAPS '),
     ('ChildrensRidingWear','Childrens Riding Wear'),('Helmets','Helmets'),
     ('Gloves','Gloves'),('WomensTights&Breeches','WomensTights&Breeches'),
     ('BodyProtectors','Body Protectors'),
    ('WomensRidingClothing','Womens Riding Clothing'),
  
    ]
    name=models.CharField(max_length= 200)
    content=models.TextField(blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)
    category =models.CharField(max_length= 200,null=True,blank=True,choices=categoryList)
    def __str__(self):
        return self.name
    class Meta:   
        verbose_name='product_table'
        ordering=['-price']

class Comment(models.Model):
 
    body=models.TextField(verbose_name='')
    comment_daate=models.DateTimeField(auto_now=True)
    product =models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    def __str__(self):
        return self.body
    class Meta:   
        verbose_name='Comment_table'    
        ordering=['-comment_daate']
