# from django.db import models

# # Create your models here.

# class Cita(models.Model):
#     fecha_hora = models.DateTimeField()
#     paciente = models.CharField(max_length=100, editable=False)  # No editable
#     tipo_cita = models.CharField(max_length=50, choices=[
#         ('Consulta', 'Consulta'),
#         ('Servicio', 'Servicio'),
#         ('Tratamiento', 'Tratamiento'),
#     ])
#     medico = models.CharField(max_length=100)
#     numero_cita = models.AutoField(primary_key=True)  # No editable
#     eliminada = models.BooleanField(default=False)  # Para "eliminar" sin borrar

#     def __str__(self):
#         return f"{self.numero_cita} - {self.paciente} ({self.tipo_cita})"
    
from django.db import models

class Cita(models.Model):
    TIPOS_CITA = [
        ('Consulta', 'Consulta'),
        ('Servicio', 'Servicio'),
        ('Tratamiento', 'Tratamiento'),
        ('Otra', 'Otra'),
    ]

    fecha_hora = models.DateTimeField()
    paciente = models.CharField(max_length=100, editable=False)  # No editable
    tipo_cita = models.CharField(max_length=50, choices=TIPOS_CITA)  # Menú desplegable
    tipo_cita_personalizado = models.CharField(max_length=100, blank=True, null=True)  # Campo extra para "Otra"
    medico = models.CharField(max_length=100)
    numero_cita = models.AutoField(primary_key=True)  # No editable
    eliminada = models.BooleanField(default=False)  # Para "eliminar" sin borrar

    def __str__(self):
        return f"{self.numero_cita} - {self.paciente} ({self.tipo_cita if self.tipo_cita != 'Otra' else self.tipo_cita_personalizado})"

