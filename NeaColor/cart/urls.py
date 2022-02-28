from unicodedata import name
from django.urls import path
from cart import views
from .models import Producto
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cart'

urlpatterns = [
    path('<slug>/', views.ProductoDetalle.as_view(), name="producto"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)