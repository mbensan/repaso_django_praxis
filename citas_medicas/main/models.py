from django.db import models

# Create your models here.
class Contacto(models.Model):
  nombre = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  mensaje = models.TextField()

