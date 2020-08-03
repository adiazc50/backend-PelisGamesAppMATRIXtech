# Generated by Django 3.0.8 on 2020-08-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('titulo', models.CharField(max_length=30, verbose_name='tituloJ')),
                ('nombreJuego', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('ano', models.IntegerField(verbose_name='Tipo')),
                ('protagonistas', models.CharField(max_length=30, verbose_name='protagonista')),
                ('director', models.CharField(max_length=30, verbose_name='dir')),
                ('productor', models.CharField(max_length=30, verbose_name='prod')),
                ('plataforma', models.CharField(max_length=30, verbose_name='tecnologia')),
                ('precio', models.IntegerField(verbose_name='costo')),
            ],
        ),
    ]
