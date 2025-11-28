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


class Estadia(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    observaciones = models.TextField(blank=True)