from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Core import views
from cart.models import Producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='home'),
    path('cuenta/', include('django.contrib.auth.urls')),
    path('registro/usuario/', views.RegistroConsumidorFinal.as_view(), name='registroUsuario'),
    path('registro/empresa/', views.RegistroEmpresa.as_view(), name='registroEmpresa'),
    path('contacto/', views.Contacto.as_view(), name='contacto'),
    path('nosotros/',views.Nosotros.as_view(), name='nosotros'),
    path('blogs/', views.Blogs.as_view(), name='blogs'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('producto/', include('cart.urls', namespace='cart')),
    path('historial/', views.Historial.as_view(), name="historial"),
    path('carrito/', views.CarritoView.as_view(), name="carrito"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)