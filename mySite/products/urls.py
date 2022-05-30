from . import views
from django.urls import path

urlpatterns = [
 path('product', views.product,name='product'),
 path('', views.products,name='products'),
  path('book', views.book,name='book'),

]