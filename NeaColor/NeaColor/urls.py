from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('cuenta/', include('django.contrib.auth.urls')),
    path('registro/usuario/', views.RegistroConsumidorFinal.as_view(), name='registroUsuario'),
    path('registro/empresa/', views.RegistroEmpresa.as_view(), name='registroEmpresa'),
    path('contacto/', views.Contacto.as_view(), name='contacto'),
    path('nosotros/',views.Nosotros.as_view(), name='nosotros'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('producto/', views.Producto.as_view(), name="producto")

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)