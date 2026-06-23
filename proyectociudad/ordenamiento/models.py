from django.db import models

class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    num_viviendas = models.IntegerField()
    num_parques = models.IntegerField(choices=[(i, str(i)) for i in range(1, 7)])
    num_edificios = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return self.nombre

class Presidente(models.Model):
    cedula = models.CharField(max_length=20)
    nickname = models.CharField(max_length=50)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)
    barrio = models.OneToOneField(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname