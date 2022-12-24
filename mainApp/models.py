from django.db import models

class Bloques (models.Model):
    duracion_inicio = models.TimeField()
    duracion_termino = models.TimeField()
    orden = models.IntegerField()

    def __int__(self):
        return self.orden

class Docente (models.Model):
    nombre = models.CharField(max_length=40)
    rut_docente = models.CharField(max_length=20)
    email_docente = models.EmailField(max_length=50)
    duracion_inicios = models.TimeField()
    duracion_terminos = models.TimeField()
    nombre_dia = models.CharField(max_length=20)
    orden_dia = models.IntegerField()
    asignaturas = models.CharField(max_length=60)
    sala = models.IntegerField()
    
    def __str__(self):
         return self.nombre + " (" + str(self.rut_docente) + ")"

class Dias (models.Model):
    nombre_dia = models.CharField(max_length=20)
    orden_dia = models.IntegerField()

    def __str__(self):
         return self.nombre_dia

class Bloque_dias (models.Model):
    asignatura = models.CharField(max_length=60)
    sala = models.IntegerField()
    bloque = models.ForeignKey(Bloques,null=True,blank=True,on_delete=models.CASCADE)
    dia = models.ForeignKey(Dias,null=True,blank=True,on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
         return self.asignatura

