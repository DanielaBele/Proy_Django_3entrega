from django.db import models

# Create your models here.
class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)  # Ej: perro, gato, conejo
    raza = models.CharField(max_length=100, blank=True)
    edad = models.IntegerField()
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class Estadía(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.mascota.nombre} - {self.fecha_ingreso} a {self.fecha_salida or 'actual'}"