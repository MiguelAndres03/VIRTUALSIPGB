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

class Referencias (models.Model):
    Identificador_Referencia = models.AutoField(primary_key=True)

class Categorias (models.Model):
    Nombre_Categoria = models.CharField(max_length=100)
    

class Libros (models.Model):
    categorias = models.ForeignKey(Categorias,null=False, blank=False, on_delete=models.CASCADE)
    Codigo_Libro = models.CharField(max_length=10)
    Titulo = models.CharField(max_length=100)
    Autor = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)

class Estudiantes (models.Model):
    Tipo_Documento = models.CharField(max_length=30)
    Numero_Identificacion = models.CharField(max_length=40)
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)

class Carreras (models.Model):
    Codigo_Carrera = models.CharField(max_length=10)
    Nombre_Carrera = models.CharField(max_length=100)


class Prestamos (models.Model):
    Fecha_Prestamo = models.DateField()
    Estado_Prestamo = models.CharField(max_length=50)

class Renovacion (models.Model):
    Fecha_Renovacion = models.DateField()

class Devoluciones (models.Model):
    Fecha_Devolucion = models.DateField()


