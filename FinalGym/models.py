from django.db import models
from django.contrib.auth.models import User

class Clase(models.Model):
    nombre=models.CharField(max_length=30)
    camada=models.IntegerField()
    duracion=models.IntegerField()

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.camada,self.nombre)

class Entrenador(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    matricula=models.IntegerField()
    clase=models.CharField(max_length=30, default="")
   
    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"

    def __str__(self):
        txt="{0} - {1}"
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Matricula: {self.matricula} - Clase: {self.clase}"


class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email= models.EmailField()
    numerocliente=models.IntegerField()
    claseinscripta=models.CharField(max_length=30, default="")

    def __str__(self):
        txt="{0} - {1}"
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Número Cliente: {self.numerocliente} - Clase Inscripta: {self.claseinscripta}"
   

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to = 'avatares', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatares'

