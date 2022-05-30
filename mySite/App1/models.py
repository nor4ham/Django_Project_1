from django.db import models


class Product(models.Model):   
    title=models.CharField(max_length=50,null=True)
    def __str__(self):
     return self.title
class user (models.Model):
    name=models.CharField(max_length=50,null=True)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
     return self.name
class Signup (models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
     return self.username  