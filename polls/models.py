from django.db import models
# Create your models here.

class Usuario (models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Tipo_Documento = models.CharField(max_length=30)
    Numero_Identificacion = models.CharField(max_length=40)
    Fecha_Nacimiento = models.DateField()
    Usuario = models.CharField(max_length=30)
    Contraseña = models.CharField(max_length=20)

class Carreras (models.Model):
    Codigo_Carrera = models.CharField(max_length=10)
    Nombre_Carrera = models.CharField(max_length=100)

class Estudiantes (models.Model):
    carreras = models.ForeignKey(Carreras, null=False, blank=False, on_delete=models.CASCADE)
    Tipo_Documento = models.CharField(max_length=30)
    Numero_Identificacion = models.CharField(max_length=40)
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)

class Categorias (models.Model):
    Nombre_Categoria = models.CharField(max_length=100)
    
class Libros (models.Model):
    categorias = models.ForeignKey(Categorias, null=False, blank=False, on_delete=models.CASCADE)
    estudiantes = models.ForeignKey(Estudiantes, null=False, blank=False, on_delete=models.CASCADE)
    Codigo_Libro = models.CharField(max_length=10)
    Titulo = models.CharField(max_length=100)
    Autor = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)

class Devoluciones (models.Model):
    Fecha_Devolucion = models.DateField()

class Referencias (models.Model):
    libros = models.ForeignKey(Libros, null=False, blank=False, on_delete=models.CASCADE)
    Identificador_Referencia = models.AutoField(primary_key=True)

class Prestamos (models.Model):
    referencia = models.OneToOneField(Referencias.Identificador_Referencia, null=False, blank=False, on_delete=models.CASCADE)
    libros = models.ForeignKey(Libros, null=False, blank=False, on_delete=models.CASCADE)
    estudiantes = models.ForeignKey(Estudiantes, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_Prestamo = models.DateField()
    Estado_Prestamo = models.CharField(max_length=50)
    
class Renovacion (models.Model):
    prestamo = models.ForeignKey(Prestamos, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_Renovacion = models.DateField()
