from django.contrib import admin

from .models import Usuario
from .models import Libros
from .models import Categorias
from .models import Estudiantes
from .models import Carreras
from .models import Referencias
from .models import Prestamos
from .models import Renovacion
from .models import Devoluciones

admin.site.register(Usuario)
admin.site.register(Libros)
admin.site.register(Categorias)
admin.site.register(Estudiantes)
admin.site.register(Carreras)
admin.site.register(Referencias)
admin.site.register(Prestamos)
admin.site.register(Renovacion)
admin.site.register(Devoluciones)


# Register your models here.
