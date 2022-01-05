from django.urls import path
from cart import views
from .models import Producto
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cart'

urlpatterns = [
    path('<slug>/', views.Producto.as_view(), name="producto")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)