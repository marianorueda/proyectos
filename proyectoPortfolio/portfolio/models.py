from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField(blank=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True)

    def __str__(self):
        return str(self.titulo)