from django.db import models


# Create your models here.

class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True)
    nombreCliente = models.CharField(verbose_name='nombreC',max_Length=20)
    direccion = models.CharField(verbose_name='dir',max_Length=20)
    telefono = models.CharField(verbose_name='tel',max_Length=20)
    celular = models.CharField(verbose_name='cel',max_Length=20)
    email = models.EmailField(verbose_name='correo',max_Length=20)

    def __str__(self):
        return 

class Prestamo(models.Model):
    idPrestamos=models.AutoField(verbose_name='idP',primary_key=True)
    nombreCliente=models.CharField(verbose_name='NombreCl',max_Length=20)
    idCliente=models.IntegerField(verbose_name='idC')
    nombreJuego=models.CharField(verbose_name='NombreJ',max_Length=20)
    fechaPrestamo=models.DateTimeField(verbose_name='Fechap',auto_now_add=True)
    fechaVence=models.DateField(verbose_name='fechaV')
    Correo=models.CharField(verbose_name='correoP',max_Length=20)
    


class Juegos(models.Model):
    titulo=models.CharField(verbose_name='tituloJ',max_Length=20)
    nombreJuego=models.CharField(primary_key=True,max_Length=20)
    ano=models.IntegerField(verbose_name='Tipo')
    protagonistas=models.CharField(verbose_name='protagonista',max_Length=50)
    director=models.CharField(verbose_name='dir',max_Length=20)
    productor=models.CharField(verbose_name='prod',max_Length=20)
    plataforma=models.CharField(verbose_name='tecnologia',max_Length=20)
    precio= models.IntegerField(verbose_name='costo')