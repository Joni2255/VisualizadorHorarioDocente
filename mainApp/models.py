from django.db import models

class Bloques (models.Model):
    duracion_inicio = models.DurationField()
    duracion_termino = models.DurationField()
    orden = models.IntegerField()


class Docente (models.Model):
    nombre = models.CharField(max_length=40)
    rut_docente = models.CharField(max_length=20)
    email_docente = models.CharField(max_length=50)

class Dias (models.Model):
    nombre_dia = models.CharField(max_length=20)
    orden_dia = models.IntegerField()

class Bloque_dias (models.Model):
    asignatura = models.CharField(max_length=60)
    sala = models.IntegerField()
    bloque = models.ForeignKey(Bloques,null=True,blank=True,on_delete=models.CASCADE)
    dia = models.ForeignKey(Dias,null=True,blank=True,on_delete=models.CASCADE)