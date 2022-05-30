
from xml.dom.expatbuilder import DOCUMENT_NODE
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('App1.urls')),
    path('products/', include('products.urls')),
     
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
