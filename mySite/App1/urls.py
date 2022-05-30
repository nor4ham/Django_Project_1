from . import views
from django.urls import path

urlpatterns = [
 path('', views.home,name='home'),
 path('about/', views.about,name='about'),
 path('login/', views.login,name='login'),
 path('signup/', views.signup,name='signup'),

]