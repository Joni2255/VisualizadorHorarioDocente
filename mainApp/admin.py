from django.contrib import admin
from mainApp.models import Bloques, Docente, Dias, Bloque_dias

class BloquesAdmin(admin.ModelAdmin):
    list_display = ["duracion_inicio","duracion_termino","orden"]

admin.site.register(Bloques, BloquesAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ["nombre","rut_docente","email_docente", "duracion_inicios", "duracion_terminos", "nombre_dia", "orden_dia", "asignaturas", "sala"]

admin.site.register(Docente, DocenteAdmin)

class DiasAdmin(admin.ModelAdmin):
    list_display = ["nombre_dia","orden_dia"]

admin.site.register(Dias, DiasAdmin)

class BloqueDiasAdmin(admin.ModelAdmin):
    list_display = ["asignatura","sala","bloque","dia","docente"]

admin.site.register(Bloque_dias, BloqueDiasAdmin)

