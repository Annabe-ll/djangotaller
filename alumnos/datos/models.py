from django.db import models

# Create your models here.
class InfoGeneral(models.Model):
	nombre = models.CharField(max_length=50, default="Juanito")
	apellido = models.CharField(max_length=50, default="")
	telefono = models.CharField(max_length=50, default="")
	fecha_nacimiento = models.DateField()
	semestre = models.IntegerField()
	carrera = models.CharField(max_length=50)
	SEXO_OPTION = (
		('F', 'Femenino'),
		('M', 'Masculino'),
		)
	sexo = models.CharField(max_length=2, choices=SEXO_OPTION)
	direccion = models.CharField(max_length=100)
	estarura = models.CharField(max_length=100, default="")


