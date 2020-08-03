from django.db import models
import uuid


class Cliente(models.Model):
    idCliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombreCliente = models.CharField(verbose_name='nombre', max_length=30)
    direccion = models.CharField(verbose_name='dir', max_length=30)
    telefono = models.CharField(verbose_name='tel', max_length=30)
    celular = models.CharField(verbose_name='cel', max_length=30)
    email = models.EmailField(verbose_name='correo', max_length=30)


class Prestamo(models.Model):
    idPrestamos=models.AutoField(primary_key=True)
    nombreCliente=models.CharField(verbose_name='NombreCl',max_length=30)
    idCliente=models.IntegerField(verbose_name='idC')
    nombreJuego=models.CharField(verbose_name='NombreJ',max_length=30)
    fechaPrestamo=models.DateTimeField(verbose_name='Fechap',auto_now_add=True)
    fechaVence=models.DateField(verbose_name='fechaV')
    Correo=models.CharField(verbose_name='correoP',max_length=30)
    


class Juegos(models.Model):
    titulo=models.CharField(verbose_name='tituloJ',max_length=30)
    nombreJuego=models.CharField(primary_key=True,max_length=30)
    ano=models.IntegerField(verbose_name='Tipo')
    protagonistas=models.CharField(verbose_name='protagonista',max_length=30)
    director=models.CharField(verbose_name='dir',max_length=30)
    productor=models.CharField(verbose_name='prod',max_length=30)
    plataforma=models.CharField(verbose_name='tecnologia',max_length=30)
    precio= models.IntegerField(verbose_name='costo')