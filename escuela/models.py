from django.db import models

class Carrera(models.Model):
	nombre = models.CharField(max_length=100, verbose_name="Nombre")

	def __str__(self): 
		return self.nombre	

class Alumno(models.Model):
	nombre = models.CharField(max_length=50, verbose_name="Nombre")
	apellidoPaterno = models.CharField(max_length=100, verbose_name="Apellido Paterno")
	apellidoMaterno = models.CharField(max_length=100, verbose_name="Apellido Materno")
	carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

	def __str__(self): 
		return self.nombre