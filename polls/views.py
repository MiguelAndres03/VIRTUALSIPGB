from django.shortcuts import render
from rest_framework import  serializers, viewsets

from .serializers import UsuarioSerializer
from .serializers import CarrerasSerializer
from .serializers import EstudiantesSerializer
from .serializers import CategoriasSerializer
from .serializers import LibrosSerializer
from .serializers import ReferenciasSerializer
from .serializers import PrestamosSerializer
from .serializers import RenovacionSerializer
from .serializers import DevolucionesSerializer
from .models import Usuario
from .models import Carreras
from .models import Estudiantes
from .models import Categorias
from .models import Libros
from .models import Referencias
from .models import Prestamos
from .models import Renovacion
from .models import Devoluciones

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CarrerasViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    serializer_class = CarrerasSerializer

class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer

class ReferenciasViewSet(viewsets.ModelViewSet):
    queryset = Referencias.objects.all()
    serializer_class = ReferenciasSerializer

class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = Prestamos.objects.all()
    serializer_class = PrestamosSerializer

class RenovacionViewSet(viewsets.ModelViewSet):
    queryset = Renovacion.objects.all()
    serializer_class = RenovacionSerializer

class DevolucionesViewSet(viewsets.ModelViewSet):
    queryset = Devoluciones.objects.all()
    serializer_class = DevolucionesSerializer
# Create your views here.
