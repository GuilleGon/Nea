from functools import partial
from unicodedata import name
from django.urls import path
from cart import views
from .models import Producto
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cart'

urlpatterns = [
    path('checkout/', views.Checkout.as_view(), name="checkout"),
    path('<slug>/', views.ProductoDetalle.as_view(), name="producto"),
    path('', views.CartView.as_view(), name="carrito"),
    path('incrementar-item/<pk>/', views.IncrementarCantidad.as_view(), name="incrementar"),
    path('decrementar-item/<pk>/', views.DecrementarCantidad.as_view(), name="decrementar"),
    path('borrar-item/<pk>/', views.BorrarItem.as_view(), name="borrar"),
    path('mercado-api/', views.MercadoApi.as_view(), name='mercado-api')
    

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)