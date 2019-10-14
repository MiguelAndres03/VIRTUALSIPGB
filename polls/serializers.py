from rest_framework import  serializers, viewsets

from polls.models import Usuario
from polls.models import Carreras
from polls.models import Estudiantes
from polls.models import Categorias
from polls.models import Libros
from polls.models import Referencias
from polls.models import Prestamos
from polls.models import Renovacion
from polls.models import Devoluciones

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['Nombre', 'Apellido', 'Tipo_Documento', 'Numero_Identificacion', 'Fecha_Nacimiento', 'Usuario', 'Contraseña',]

class CarrerasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carreras
        fields = ['Codigo_Carrera', 'Nombre_Carrera',]

class EstudiantesSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        carreras = CarrerasSerializer (many = False)
        model = Estudiantes
        fields = ['carreras', 'Tipo_Documento','Numero_Identificacion','Nombre','Apellido',]

class CategoriasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorias
        fields = ['Nombre_Categoria','descripcion',]

class LibrosSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        categorias = CategoriasSerializer (many = False)
        estudiantes = EstudiantesSerializer (many = False)
        model = Libros
        fields = ['categorias', 'estudiantes','Codigo_Libro','Titulo','Autor','Editorial',]

class ReferenciasSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        libros = LibrosSerializer (many = False)
        model = Referencias
        fields = ['libros', 'Identificador_Referencia',]

class PrestamosSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        referencia = ReferenciasSerializer (many = False)
        libros = LibrosSerializer (many = False)
        estudiantes = EstudiantesSerializer (many = False)
        model = Prestamos
        fields = ['referencia', 'libros','estudiantes','Fecha_Prestamo', 'Estado_Prestamo']

class RenovacionSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        prestamo = PrestamosSerializer (many = False)
        model = Renovacion
        fields = ['prestamo', 'Fecha_Renovacion',]

class DevolucionesSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        prestamo = PrestamosSerializer (many = False)
        model = Devoluciones
        fields = ['prestamo', 'Fecha_Devolucion',]