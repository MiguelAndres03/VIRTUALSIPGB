from django.db import models

# Create your models here.

class Usuario (models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    IDENTIFICACION = (('CC','Cedula de Ciudadania') , ('TI','Tarjeta de Identidad') ,('TP','Tarjeta de Pasaporte') ,('RC','Registro Civil'),('CE','Cedula de Extranjeria'))
    Tipo_Documento = models.CharField(max_length=2, choices=IDENTIFICACION, default='CC')
    Numero_Identificacion = models.CharField(max_length=40)
    Fecha_Nacimiento = models.DateField()
    Usuario = models.CharField(max_length=30)
    Contraseña = models.CharField(max_length=20)

    def NombreCompleto(self):
        cadena ="{0} {1}"
        return cadena.format(self.Nombre, self.Apellido)

    def __str__(self): 
        return self.NombreCompleto()

class Carreras (models.Model):
    Codigo_Carrera = models.CharField(max_length=10)
    Nombre_Carrera = models.CharField(max_length=100)

    def NombreCarrera(self):
        cadena ="{0} {1}"
        return cadena.format(self.Codigo_Carrera, self.Nombre_Carrera)

    def __str__(self):
        return self.NombreCarrera()

class Estudiantes (models.Model):
    carreras = models.ForeignKey(Carreras, null=True, blank=False, on_delete=models.CASCADE)
    IDENTIFICACION = (('CC','Cedula de Ciudadania') , ('TI','Tarjeta de Identidad') ,('TP','Tarjeta de Pasaporte') ,('RC','Registro Civil'),('CE','Cedula de Extranjeria'))
    Tipo_Documento = models.CharField(max_length=2, choices=IDENTIFICACION, default='CC')
    Numero_Identificacion = models.CharField(max_length=40)
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)

    def NombreCompleto(self):
        cadena ="{0} {1}"
        return cadena.format(self.Nombre, self.Apellido)

    def __str__(self): 
        return self.NombreCompleto()

class Categorias (models.Model):
    Nombre_Categoria = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    def __str__(self):
        return self.Nombre_Categoria
    
class Libros (models.Model):
    categorias = models.ForeignKey(Categorias, null=True, blank=False, on_delete=models.CASCADE)
    estudiantes = models.ForeignKey(Estudiantes, null=True, blank=False, on_delete=models.CASCADE)
    Codigo_Libro = models.CharField(max_length=10)
    Titulo = models.CharField(max_length=100)
    Autor = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)

    def NombreLibro(self):
        cadena ="{0} {1}"
        return cadena.format(self.Codigo_Libro, self.Titulo)

    def __str__(self):
        return self.NombreLibro()

class Referencias (models.Model):
    libros = models.ForeignKey(Libros, null=True, blank=False, on_delete=models.CASCADE)
    Identificador_Referencia = models.AutoField(primary_key=True)

class Prestamos (models.Model):
    referencia = models.OneToOneField(Referencias, null=True, blank=False, on_delete=models.CASCADE)
    libros = models.ForeignKey(Libros, null=True, blank=False, on_delete=models.CASCADE)
    estudiantes = models.ForeignKey(Estudiantes, null=True, blank=False, on_delete=models.CASCADE)
    Fecha_Prestamo = models.DateField()
    Estado_Prestamo = models.CharField(max_length=50)

class Renovacion (models.Model):
    prestamo = models.ForeignKey(Prestamos, null=True, blank=False, on_delete=models.CASCADE)
    Fecha_Renovacion = models.DateField()

class Devoluciones (models.Model):
    prestamo = models.OneToOneField(Prestamos, null=True, blank=False, on_delete=models.CASCADE)
    Fecha_Devolucion = models.DateField()
