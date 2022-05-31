from . import views
from django.urls import path
from .models import Product

urlpatterns = [
path('delete_product/<id>', views.delete_product,name='delete_product'),
 path('product/<id>', views.product,name='product'),
 path('', views.products,name='products'),
 path('book', views.book,name='book'),
 path('PostersPrints', views.PostersPrints,name='PostersPrints'),
 path('RIDINGBOOTS', views.RIDINGBOOTS,name='RIDINGBOOTS'),
 path('ChildrensRidingWear', views.ChildrensRidingWear,name='ChildrensRidingWear'),
 path('Helmets', views.Helmets,name='Helmets'),
 path('Gloves', views.Gloves,name='Gloves'),
 path('WomensTightsBreeches', views.WomensTightsBreeches,name='WomensTightsBreeches'),
 path('BodyProtectors', views.BodyProtectors,name='BodyProtectors'),
 path('WomensRidingClothing', views.WomensRidingClothing,name='WomensRidingClothing'),
]