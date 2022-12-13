from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class autor(models.Model):

    nombre = models.CharField(max_length=40)

    titulo = models.CharField(max_length=40)

    email = models.EmailField(default='test@test.com')

    fecha = models.DateField(default=datetime.now)

    subtitulo = models.CharField(max_length=100,blank=True)

    post = models.TextField("")

    def __str__(self):
        return f' {self.nombre} {self.titulo} {self.email} {self.fecha} {self.subtitulo} {self.post}'


class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    