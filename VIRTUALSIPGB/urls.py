"""VIRTUALSIPGB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from polls.models import Usuario, Carreras, Estudiantes, Categorias, Libros, Referencias, Prestamos, Renovacion, Devoluciones
from polls.views import UsuarioViewSet
from polls.views import CarrerasViewSet
from polls.views import EstudiantesViewSet
from polls.views import CategoriasViewSet
from polls.views import LibrosViewSet
from polls.views import ReferenciasViewSet
from polls.views import PrestamosViewSet
from polls.views import RenovacionViewSet
from polls.views import DevolucionesViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'carreras', CarrerasViewSet)
router.register(r'estudiantes', EstudiantesViewSet)
router.register(r'categorias', CategoriasViewSet)
router.register(r'libros', LibrosViewSet)
router.register(r'referencias', ReferenciasViewSet)
router.register(r'prestamos', PrestamosViewSet)
router.register(r'renovacion', RenovacionViewSet)
router.register(r'devoluciones', DevolucionesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
